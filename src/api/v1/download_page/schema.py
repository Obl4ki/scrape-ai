from pydantic import BaseModel


class GetPageContentRequest(BaseModel):
    """Request model for page content retrieval."""

    url: str


class GetPageContentResponse(BaseModel):
    """Response model for page content retrieval."""

    url: str
    content: str


class GetPageContentErrorResponse(BaseModel):
    """Error response model for page content retrieval."""

    detail: str
