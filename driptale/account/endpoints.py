from fastapi import APIRouter, Depends, Request, status

from driptale.account.schemas import AccountCreate, AccountResponse
from driptale.account.service import AccountService
from driptale.dependencies import get_account_service
from driptale.firebase import verify_firebase_token
from driptale.rate_limiter import limiter

router = APIRouter(tags=["Profile API endpoints"])


@router.post(
    "/account", summary="Create a new account", status_code=status.HTTP_201_CREATED
)
@limiter.limit("5/minute")
def create_account(
    request: Request,
    payload: AccountCreate,
    user_id: str = Depends(verify_firebase_token),
    service: AccountService = Depends(get_account_service),
) -> AccountResponse:
    """Create a new account."""
    return service.create_account(payload, user_id)
