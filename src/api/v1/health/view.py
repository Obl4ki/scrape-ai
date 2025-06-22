from api.v1.health.schema import HealthResponse
from fastapi import APIRouter


router = APIRouter(
    tags=["health"],
)


@router.get("/health")
def health_check():
    """Health check endpoint."""
    return HealthResponse(status="ok")
