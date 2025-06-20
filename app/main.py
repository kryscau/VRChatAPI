from fastapi import FastAPI
from app.api.vrchat_public import router as routerPublic
from app.api.vrchat_private import router as routerPrivate

app = FastAPI(title="K-API - VRChat API Proxy")
prefix = "/api"

app.include_router(routerPublic, prefix=prefix, tags=["VRChat - Public"])
app.include_router(routerPrivate, prefix=prefix, tags=["VRChat - Private"])