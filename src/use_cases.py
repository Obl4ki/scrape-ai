import requests

from api.v1.download_page.error import DownloadPageException
from utils import generate_headers
from db import create_scraped_site


def download_page_content(url: str) -> str:
    """Retrieve the content of a web page."""
    try:
        response = requests.get(
            url,
            headers=generate_headers(),
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise DownloadPageException from e


def cache_to_db(url: str, content: str) -> None:
    """Cache the page content to the database."""

    try:
        create_scraped_site(url, content)
    except Exception as e:
        raise DownloadPageException(f"Failed to cache content for {url}") from e
