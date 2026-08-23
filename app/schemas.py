from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ReportCreate(BaseModel):
    name: str
    status: str
    query: str
    
class ReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    status: str
    query: str
    created_at: datetime

class ReportUpdate(BaseModel):
    name: str
    status: str
    query: str

class ReportRunResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    report_id: int
    status: str
    started_at: datetime
    completed_at: datetime | None = None
    error_message: str | None = None

class ReportRunFail(BaseModel):
    error_message: str

class ReportResultResponse(BaseModel):
    id: int
    run_id: int
    columns: list
    rows: list
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)