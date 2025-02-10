from fastapi import FastAPI
from app.api import endpoints as health_router

app = FastAPI()

app.include_router(health_router.app, prefix="/v1", tags=["migration-poc"])
