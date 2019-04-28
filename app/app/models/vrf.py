from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, validator, constr
from app.models.interface import InterfaceBase


# Shared properties
class VRFBase(BaseModel):
    name: constr(regex=r"^([a-zA-Z\-_]{3,31})$") = "default"
    interface: Optional[List[InterfaceBase]] = None

    @validator("name")
    def transform(cls, v):
        return v.upper()


class VRFBaseInDB(VRFBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class VRFInCreate(VRFBase):
    pass


# Properties to receive via API on update
class VRFInUpdate(VRFBase):
    pass


# Additional properties to return via API
class VRF(VRFBaseInDB):
    pass


# Additional properties stored in DB
class VRFInDB(VRFBaseInDB):
    pass
