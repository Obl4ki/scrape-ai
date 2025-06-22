from fastapi import FastAPI

from api.v1 import router as v1_router

VERSION = "0.0.1"

app = FastAPI(
    title="ScrapeAI",
    description="Automatic webscraping using LLMs",
    version=VERSION,
)

app.include_router(v1_router)
