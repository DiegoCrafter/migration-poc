from fastapi import FastAPI
from app.api import endpoints as health_router

app = FastAPI()


app.include_router(health_router.router, prefix="/v1", tags=["health"])
