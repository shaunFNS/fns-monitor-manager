from fastapi import APIRouter

from app.models.ping import PingMonitor
from app.services.ping import create_ping

router = APIRouter()


@router.post("/ping")
def create_ping_monitor(request: PingMonitor):

    create_ping(
        request.group,
        request.name,
        request.hostname,
    )

    return {
        "success": True
    }