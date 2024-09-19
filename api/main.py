from fastapi import FastAPI

from api import v1
from api import v2


app = FastAPI(docs_url=None, redoc_url=None)


app.include_router(v1.router, prefix="/v1")
app.include_router(v2.router, prefix="/v2")

app.mount("/v1", v1.docs)
app.mount("/v2", v2.docs)
