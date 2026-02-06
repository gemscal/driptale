from fastapi import APIRouter

from driptale.account.endpoints import router as account_router
from driptale.health.endpoints import router as health_router
from driptale.wardrobe.endpoints import router as wardrobe_router

router = APIRouter(prefix="/v1")

# /health
router.include_router(health_router)
# /account
router.include_router(account_router)
# /wardrobe
router.include_router(wardrobe_router)
