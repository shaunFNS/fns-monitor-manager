from pydantic import BaseModel

class HttpMonitor(BaseModel):
    group: str
    name: str
    url: str