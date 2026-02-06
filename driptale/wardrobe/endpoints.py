from fastapi import APIRouter, Depends, Request, status

from driptale.dependencies import get_wardrobe_service
from driptale.firebase import verify_firebase_token
from driptale.rate_limiter import limiter
from driptale.wardrobe.schemas import WardrobeCreate, WardrobeResponse
from driptale.wardrobe.service import WardrobeService

router = APIRouter(tags=["Wardrobe API endpoints"])


@router.post(
    "/wardrobe", summary="Create a new wardrobe", status_code=status.HTTP_201_CREATED
)
@limiter.limit("5/minute")
def create_wardrobe(
    request: Request,
    payload: WardrobeCreate,
    user_id: str = Depends(verify_firebase_token),
    service: WardrobeService = Depends(get_wardrobe_service),
) -> WardrobeResponse:
    """Create a new wardrobe."""
    return service.create_wardrobe(payload, user_id)
