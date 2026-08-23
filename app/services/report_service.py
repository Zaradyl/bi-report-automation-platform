from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Report, ReportRun, ReportResult


def run_report_background(
    report_id: int,
    run_id: int,
):
    db: Session = SessionLocal()

    try:
        report = db.get(Report, report_id)
        run = db.get(ReportRun, run_id)

        if not report:
            print(f"Report {report_id} not found")
            return

        if not run:
            print(f"Report run {run_id} not found")
            return

        print(f"Running report: {report.name}")

        result = db.execute(text(report.query))

        columns = list(result.keys())
        rows = [list(row) for row in result.fetchall()]

        print(f"Query returned {len(rows)} rows")
        print(rows)

        report_result = ReportResult(
            run_id=run.id,
            columns=columns,
            rows=rows,
        )

        db.add(report_result)

        run.status = "completed"
        run.completed_at = datetime.utcnow()
        run.error_message = None

        db.commit()

        print(f"Saved report result for run {run.id}")
        print(f"Finished report: {report.name}")

    except Exception as e:
        db.rollback()

        run = db.get(ReportRun, run_id)

        if run:
            run.status = "failed"
            run.completed_at = datetime.utcnow()
            run.error_message = str(e)[:1000]

            db.commit()

        print(f"Report failed")
        print(f"Error: {e}")

    finally:
        db.close()


def get_report_result(
    db: Session,
    report_id: int,
    run_id: int,
):
    report = db.get(Report, report_id)

    if report is None:
        raise ValueError("Report not found")

    run = (
        db.query(ReportRun)
        .filter(ReportRun.id == run_id)
        .filter(ReportRun.report_id == report_id)
        .first()
    )

    if run is None:
        raise ValueError("Report run not found")

    result = (
        db.query(ReportResult)
        .filter(ReportResult.run_id == run_id)
        .first()
    )

    if result is None:
        raise ValueError("Report result not found")

    return report, run, result