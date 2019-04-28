from fastapi import APIRouter
from app.api.api_v1.endpoints import (
    autonomous,
    brand,
    customer,
    location,
    device,
    vrf,
    timeline,
)

api_router = APIRouter()
api_router.include_router(location.router, prefix="/location")
api_router.include_router(customer.router, prefix="/customer")
api_router.include_router(brand.router, prefix="/brand")
api_router.include_router(device.router, prefix="/device")
api_router.include_router(vrf.router, prefix="/vrf")
api_router.include_router(autonomous.router, prefix="/autonomous_system")
api_router.include_router(timeline.router, prefix="/timeline")
