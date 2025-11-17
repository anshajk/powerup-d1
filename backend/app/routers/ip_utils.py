from fastapi import APIRouter
from app.models.ip_utils import IPClassification

router = APIRouter(prefix="/ip-utils", tags=["ip-utils"])


@router.get("/{ip_address}/type", response_model=IPClassification)
async def classify_ip(ip_address: str):
    # Simple private IP detection logic per specification
    if ip_address.startswith("10.") or ip_address.startswith("192.168."):
        ip_type = "Private"
    else:
        ip_type = "Public"
    return IPClassification(ip=ip_address, type=ip_type)
