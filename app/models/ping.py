from pydantic import BaseModel


class PingMonitor(BaseModel):
    group: str
    name: str
    hostname: str