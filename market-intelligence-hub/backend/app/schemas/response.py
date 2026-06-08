from pydantic import BaseModel
from typing import Any

class ReportResponse(BaseModel):
    title: str
    content: Any
