from fastapi import APIRouter

health_router = APIRouter()
router = APIRouter(prefix='/v1')

@health_router.get('/health')
async def health():
    return {"status": "ok", "app_name": "documind"}

