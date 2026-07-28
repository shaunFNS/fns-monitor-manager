from pydantic import BaseModel


class PingTarget(BaseModel):
    name: str
    hostname: str


class DeployClient(BaseModel):
    client: str
    website: str
    ping_targets: list[PingTarget] = []