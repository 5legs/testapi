from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator


# Shared properties
class BrandBase(BaseModel):
    name: Optional[str] = None

    @validator("name")
    def transform(cls, v):
        return v.capitalize()

    def __iter__(self):
        yield 'name', self.name


class BrandBaseInDB(BrandBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class BrandInCreate(BrandBase):
    pass


# Properties to receive via API on update
class BrandInUpdate(BrandBase):
    pass


# Additional properties to return via API
class Brand(BrandBaseInDB):
    pass


# Additional properties stored in DB
class BrandInDB(BrandBaseInDB):
    pass
