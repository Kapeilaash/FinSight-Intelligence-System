from pydantic import BaseModel

class ReportRequest(BaseModel):
    symbol: str
    start_date: str = None
    end_date: str = None
