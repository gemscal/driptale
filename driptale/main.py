from fastapi import FastAPI
from driptale.health.endpoints import router as health_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app.include_router(health_router)
