from fastapi import APIRouter, FastAPI

from api.v2.routers import items, users


router = APIRouter()
docs = FastAPI(
    root_path="/v2", docs_url="/docs", redoc_url="/redoc",
    title="API v2", version="2.0"
)

router.include_router(items.router, prefix="/items")
router.include_router(users.router, prefix="/users")

docs.include_router(router)
