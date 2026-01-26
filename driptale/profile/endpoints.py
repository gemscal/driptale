from fastapi import APIRouter

router = APIRouter(tags=["Profile API endpoints"])


@router.get("/profile", summary="Get profile endpoint")
def get_profile():
    return {"message": "Hello, World!"}
