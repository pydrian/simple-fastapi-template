from fastapi import APIRouter, FastAPI

from api.v1.routers import items


router = APIRouter()
docs = FastAPI(
    root_path="/v1", docs_url="/docs", redoc_url="/redoc",
    title="API v1", version="1.0"
)

router.include_router(items.router, prefix="/items")
docs.include_router(router)
