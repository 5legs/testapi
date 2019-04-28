from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.models.role import RoleEnum


# Shared properties
class InterfaceBase(BaseModel):
    name: str = None
    role: RoleEnum = RoleEnum.none


class InterfaceBaseInDB(InterfaceBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class InterfaceInCreate(InterfaceBase):
    pass


# Properties to receive via API on update
class InterfaceInUpdate(InterfaceBaseInDB):
    pass


# Additional properties to return via API
class Interface(InterfaceBaseInDB):
    pass


# Additional properties stored in DB
class InterfaceInDB(InterfaceBaseInDB):
    pass
