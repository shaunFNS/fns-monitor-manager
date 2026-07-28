from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.deploy_client import router as deploy_client_api_router
from app.api.groups import router as groups_router
from app.api.http import router as http_router
from app.api.ping import router as ping_router
from app.web.routes import router as web_router


app = FastAPI(
    title="FNS Monitor Manager",
    description="Monitoring deployment platform for Franke Network Solutions",
    version="0.2.0",
)

app.mount(
    "/static",
    StaticFiles(
        directory="/opt/fns-monitor-manager/app/static"
    ),
    name="static",
)

app.include_router(web_router)

app.include_router(
    groups_router,
    prefix="/api",
    tags=["Groups"],
)

app.include_router(
    ping_router,
    prefix="/api",
    tags=["Ping Monitors"],
)

app.include_router(
    http_router,
    prefix="/api",
    tags=["HTTP Monitors"],
)

app.include_router(
    deploy_client_api_router,
    prefix="/api",
    tags=["Client Deployment"],
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "fns-monitor-manager",
    }