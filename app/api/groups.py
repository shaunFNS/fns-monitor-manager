from fastapi import APIRouter, HTTPException

from app.models.group import GroupCreateRequest
from app.services.groups import create_group


router = APIRouter(
    prefix="/groups",
    tags=["Groups"],
)


@router.post("")
def add_group(request: GroupCreateRequest):
    try:
        return create_group(request.name)

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to create group: {exc}",
        ) from exc
