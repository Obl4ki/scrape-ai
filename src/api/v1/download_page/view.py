from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.v1.download_page.error import DownloadPageException
from api.v1.download_page.schema import (
    GetPageContentErrorResponse,
    GetPageContentRequest,
    GetPageContentResponse,
)

from use_cases import cache_to_db, download_page_content

router = APIRouter(
    prefix="/download-page",
    tags=["download_page"],
)


@router.post("/download-page")
def get_page_content(request: GetPageContentRequest):
    try:
        response = download_page_content(request.url)
    except DownloadPageException as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=GetPageContentErrorResponse(detail=str(e)),
        )

    cache_to_db(request.url, response)

    return GetPageContentResponse(url=request.url, content=response)
