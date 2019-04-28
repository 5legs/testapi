from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator, constr


# Shared properties
class LocationBase(BaseModel):
    name: constr(regex="^([A-Za-z][1-9])?$") = None
    address: Optional[str] = None

    @validator("name")
    def transform(cls, v):
        return v.upper()

    def __iter__(self):
        yield 'name', self.name
        yield 'address', self.address


class LocationBaseInDB(LocationBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class LocationInCreate(LocationBase):
    pass


# Properties to receive via API on update
class LocationInUpdate(LocationBase):
    pass


# Additional properties to return via API
class Location(LocationBaseInDB):
    pass


# Additional properties stored in DB
class LocationInDB(LocationBaseInDB):
    pass
