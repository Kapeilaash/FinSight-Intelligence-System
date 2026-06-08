from pydantic import BaseModel, Field


class ReportResponse(BaseModel):
    """Structured API response after the agent graph completes."""

    topic: str
    markdown: str = Field(..., description="Institutional-style markdown brief")
    critic_verdict: str = ""
    critic_reason: str = ""
    retry_loops: int = 0
