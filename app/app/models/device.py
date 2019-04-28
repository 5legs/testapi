from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, constr
from app.models.role import RoleEnum
from app.models.type import TypeEnum
from app.models.brand import BrandBase, Brand
from app.models.vrf import VRF
from app.models.location import LocationBase, Location


# Shared properties
class DeviceBase(BaseModel):
    fqdn: constr(
        regex=r"(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{0,62}[a-zA-Z0-9]\.)+[a-zA-Z]{2,63}$)"
    ) = None
    name: constr(strip_whitespace=True) = None
    # interfaces: List[Interface]
    role: RoleEnum = None
    type: TypeEnum = None
    serial: Optional[str] = None
    version: Optional[str] = None
    brand: BrandBase = None
    location: LocationBase = None


class DeviceBaseInDB(DeviceBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class DeviceInCreate(DeviceBase):
    pass


# Properties to receive via API on update
class DeviceInUpdate(DeviceBase):
    pass


# Additional properties to return via API
class Device(DeviceBaseInDB):
    vrf: List[VRF] = None
    pass


# Additional properties stored in DB
class DeviceInDB(DeviceBaseInDB):
    pass
