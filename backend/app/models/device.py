from pydantic import BaseModel
from typing import Dict


class Device(BaseModel):
    hostname: str
    ip: str
    vendor: str
    location: str


class DeviceCollection(BaseModel):
    devices: Dict[str, Device]
