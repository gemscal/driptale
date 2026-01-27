from fastapi import APIRouter

from driptale.health.endpoints import router as health_router
from driptale.profile.endpoints import router as profile_router

router = APIRouter(prefix="/v1")

# /health
router.include_router(health_router)
# /profile
router.include_router(profile_router)

# Intentionally unformatted code to test CI
def test_function(  x,y,z  ):
    if x==1 and y==2:
        return z+1
    else:
        return z*2
