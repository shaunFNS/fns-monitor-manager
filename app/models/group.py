from pydantic import BaseModel, Field


class GroupCreateRequest(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=150,
        examples=["Summit Counseling"],
    )
