from pydantic import BaseModel, Field


class ReportRequest(BaseModel):
    """User request for a market intelligence brief."""

    topic: str = Field(
        ...,
        min_length=1,
        max_length=400,
        description="Stock ticker or market theme (e.g. TSLA, AI semiconductors)",
    )
