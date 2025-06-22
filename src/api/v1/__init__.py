from fastapi import APIRouter

from api.v1.download_page.view import router as download_page_router
from api.v1.health.view import router as health_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(health_router)

router.include_router(download_page_router)
