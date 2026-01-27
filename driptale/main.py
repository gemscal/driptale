from fastapi import Depends, FastAPI

from driptale.api import router
from driptale.rate_limiter import setup_rate_limiting

app = FastAPI()
setup_rate_limiting(app)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app.include_router(router)
