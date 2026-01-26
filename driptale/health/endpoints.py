from fastapi import APIRouter

router = APIRouter(tags=["Health API endpoint"])


@router.get("/healthz", summary="Health check endpoint")
def healthz():
    return {"status": "ok", "message": "API is running"}
