from fastapi import FastAPI

from driptale.api import router
from driptale.rate_limiter import setup_rate_limiting

app = FastAPI()
setup_rate_limiting(app)


app.include_router(router)
