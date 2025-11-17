from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from app.db.mock_devices import MOCK_DEVICE_DB
from app.models.device import Device

router = APIRouter(prefix="/devices", tags=["devices"])


@router.get("/{hostname}", response_model=Device)
async def get_device(hostname: str):
    device_data = MOCK_DEVICE_DB.get(hostname)
    if not device_data:
        raise HTTPException(status_code=404, detail="Device not found")
    return Device(hostname=hostname, **device_data)


@router.get("/", response_model=List[Device])
async def list_devices(
    location: Optional[str] = Query(
        default=None, description="Filter devices by location"
    )
):
    devices = []
    for hostname, data in MOCK_DEVICE_DB.items():
        if location and data.get("location") != location:
            continue
        devices.append(Device(hostname=hostname, **data))
    return devices
