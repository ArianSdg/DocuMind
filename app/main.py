from fastapi import FastAPI

from app.api.routes import health_router, router

app = FastAPI()

app.include_router(health_router)
app.include_router(router)