from fastapi import FastAPI, Request

from driptale.health.endpoints import router as health_router
from driptale.rate_limiter import limiter, setup_rate_limiting

app = FastAPI()
setup_rate_limiting(app)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/testLimit")
@limiter.limit("5/minute")
def test_limit(request: Request):
    return {"message": "Hello, World!"}


app.include_router(health_router)
