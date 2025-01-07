# FastAPI application entry point

from fastapi import FastAPI

from api import v1, v2, v3


app = FastAPI(docs_url=None, redoc_url=None)


# including api versions as app sub-routers
app.include_router(v1.router, prefix="/v1")
app.include_router(v2.router, prefix="/v2")
app.include_router(v3.router, prefix="/v3")

# mount swagger docs/redoc for individual versions separately
app.mount("/v1", v1.docs)  # /v1/docs, /v1/redoc
app.mount("/v2", v2.docs)  # /v2/docs, /v2/redoc
app.mount("/v3", v3.docs)  # /v3/docs, /v3/redoc
