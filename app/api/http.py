from fastapi import APIRouter

from app.models.http import HttpMonitor
from app.services.http import create_http

router = APIRouter()

@router.post("/http")
def create_http_monitor(monitor: HttpMonitor):
    create_http(monitor)
    return {"status": "success"}