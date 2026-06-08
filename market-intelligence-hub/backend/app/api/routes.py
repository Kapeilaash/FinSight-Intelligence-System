from fastapi import APIRouter, HTTPException

from app.schemas.request import ReportRequest
from app.schemas.response import ReportResponse
from app.services.report_service import generate_report

router = APIRouter(prefix="/api", tags=["reports"])


@router.get("/test")
def test():
    return {"status": "API working"}


@router.post("/reports/generate", response_model=ReportResponse)
def generate_market_report(body: ReportRequest):
    """
    Run Research → Analyst → Critic (retry loop) → Writer and return markdown.
    """
    try:
        result = generate_report(body.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Report generation failed") from e

    return ReportResponse(
        topic=result["topic"],
        markdown=result["markdown"],
        critic_verdict=result.get("critic_verdict", ""),
        critic_reason=result.get("critic_reason", ""),
        retry_loops=int(result.get("retry_loops") or 0),
    )
