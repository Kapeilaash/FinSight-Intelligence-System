from fastapi import APIRouter

router = APIRouter()

@router.post("/generate-report")
async def generate_report(payload: dict):
    return {"message": "report generation placeholder", "input": payload}
