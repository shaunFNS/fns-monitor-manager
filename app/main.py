from fastapi import FastAPI

from app.api.groups import router as groups_router
from app.api.login import router as login_router
from app.api import ping
from app.api import http

app = FastAPI(
    title="Franke Network Solutions Monitor Manager",
    version="1.0.0",
)

app.include_router(login_router, prefix="/api")
app.include_router(groups_router, prefix="/api")
app.include_router(ping.router, prefix="/api")
app.include_router(http.router, prefix="/api")

@app.get("/", tags=["System"])
def home():
    return {
        "status": "online",
        "service": "FNS Monitor Manager",
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "healthy": True,
    }


