import io
from datetime import datetime

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from openpyxl import Workbook
from openpyxl.styles import Font
from sqlalchemy.orm import Session

from .database import get_db
from .models import Report, ReportRun
from .schemas import (
    ReportCreate,
    ReportResponse,
    ReportUpdate,
    ReportRunResponse,
    ReportRunFail,
    ReportResultResponse,
)
from .services.report_service import (
    get_report_result,
    run_report_background,
)


app = FastAPI()


# =========================
# System Endpoints
# =========================

@app.get("/")
def root():
    return {"message": "BI Report Automation Platform"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# =========================
# Report Endpoints
# =========================

@app.post("/reports", response_model=ReportResponse)
def create_report(
    report: ReportCreate,
    db: Session = Depends(get_db),
):
    new_report = Report(
        name=report.name,
        status=report.status,
        query=report.query,
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report


@app.get("/reports", response_model=list[ReportResponse])
def get_reports(
    db: Session = Depends(get_db),
):
    reports = db.query(Report).all()

    return reports


@app.get("/reports/{report_id}", response_model=ReportResponse)
def get_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    return report


@app.put("/reports/{report_id}", response_model=ReportResponse)
def update_report(
    report_id: int,
    report_data: ReportUpdate,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    report.name = report_data.name
    report.status = report_data.status
    report.query = report_data.query

    db.commit()
    db.refresh(report)

    return report


@app.delete("/reports/{report_id}")
def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    db.delete(report)
    db.commit()

    return "Report deleted successfully"


# =========================
# ReportRun Endpoints
# =========================

@app.post(
    "/reports/{report_id}/runs",
    response_model=ReportRunResponse,
)
def create_report_run(
    report_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    existing_run = (
        db.query(ReportRun)
        .filter(ReportRun.report_id == report_id)
        .filter(ReportRun.status == "processing")
        .first()
    )

    if existing_run is not None:
        raise HTTPException(
            status_code=409,
            detail="Report is already running",
        )

    new_run = ReportRun(
        report_id=report_id,
        status="processing",
        started_at=datetime.utcnow(),
    )

    db.add(new_run)
    db.commit()
    db.refresh(new_run)

    background_tasks.add_task(
        run_report_background,
        report_id,
        new_run.id,
    )

    return new_run


@app.get(
    "/reports/{report_id}/runs",
    response_model=list[ReportRunResponse],
)
def get_report_runs(
    report_id: int,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    runs = (
        db.query(ReportRun)
        .filter(ReportRun.report_id == report_id)
        .all()
    )

    return runs


@app.get(
    "/reports/{report_id}/runs/{run_id}",
    response_model=ReportRunResponse,
)
def get_report_run(
    report_id: int,
    run_id: int,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    run = (
        db.query(ReportRun)
        .filter(ReportRun.id == run_id)
        .filter(ReportRun.report_id == report_id)
        .first()
    )

    if run is None:
        raise HTTPException(
            status_code=404,
            detail="Report run not found",
        )

    return run


@app.post(
    "/reports/{report_id}/runs/{run_id}/complete",
    response_model=ReportRunResponse,
)
def complete_report_run(
    report_id: int,
    run_id: int,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    run = (
        db.query(ReportRun)
        .filter(ReportRun.id == run_id)
        .filter(ReportRun.report_id == report_id)
        .first()
    )

    if run is None:
        raise HTTPException(
            status_code=404,
            detail="Report run not found",
        )

    if run.status != "processing":
        raise HTTPException(
            status_code=409,
            detail="Report run is not processing",
        )

    run.status = "completed"
    run.completed_at = datetime.utcnow()

    db.commit()
    db.refresh(run)

    return run


@app.post(
    "/reports/{report_id}/runs/{run_id}/fail",
    response_model=ReportRunResponse,
)
def fail_report_run(
    report_id: int,
    run_id: int,
    run_data: ReportRunFail,
    db: Session = Depends(get_db),
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    run = (
        db.query(ReportRun)
        .filter(ReportRun.id == run_id)
        .filter(ReportRun.report_id == report_id)
        .first()
    )

    if run is None:
        raise HTTPException(
            status_code=404,
            detail="Report run not found",
        )

    if run.status != "processing":
        raise HTTPException(
            status_code=409,
            detail="Report run is not processing",
        )

    run.status = "failed"
    run.completed_at = datetime.utcnow()
    run.error_message = run_data.error_message

    db.commit()
    db.refresh(run)

    return run

@app.get(
    "/reports/{report_id}/runs/{run_id}/result",
    response_model=ReportResultResponse,
)
def get_report_result_endpoint(
    report_id: int,
    run_id: int,
    db: Session = Depends(get_db),
):
    try:
        report, run, result = get_report_result(
            db,
            report_id,
            run_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    return result

@app.get(
    "/reports/{report_id}/runs/{run_id}/result/excel",
)
def export_report_result_excel(
    report_id: int,
    run_id: int,
    db: Session = Depends(get_db),
):
    try:
        report, run, result = get_report_result(
            db,
            report_id,
            run_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Report"

    # Add column headers
    worksheet.append(result.columns)

    # Make headers bold
    for cell in worksheet[1]:
        cell.font = Font(bold=True)

    # Add report data
    for row in result.rows:
        worksheet.append(row)

    # Freeze the header row
    worksheet.freeze_panes = "A2"

    # Add filters
    worksheet.auto_filter.ref = worksheet.dimensions

    # Automatically size columns
    for column in worksheet.columns:
        max_length = 0

        for cell in column:
            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value)),
                )

        column_letter = column[0].column_letter

        worksheet.column_dimensions[column_letter].width = (
            max_length + 2
        )

    output = io.BytesIO()

    workbook.save(output)
    output.seek(0)

    filename = f"{report.name}_run_{run_id}.xlsx"

    return StreamingResponse(
        output,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        },
    )