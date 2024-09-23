# FastAPI application entry point

from fastapi import FastAPI

from api import v1
from api import v2


app = FastAPI(docs_url=None, redoc_url=None)


# including api versions as app sub-routers
app.include_router(v1.router, prefix="/v1")
app.include_router(v2.router, prefix="/v2")

# mount swagger docs/redoc for individual versions separately
app.mount("/v1", v1.docs)  # /v1/docs, /v1/redoc
app.mount("/v2", v2.docs)  # /v2/docs, /v2/redoc
