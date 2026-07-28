from pydantic import BaseModel, Field


class PingTarget(BaseModel):
    name: str
    hostname: str


class DeployClient(BaseModel):
    client: str
    website: str
    ping_targets: list[PingTarget] = Field(
        default_factory=list,
    )