from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.models.customer import Customer


# Shared properties
class TimelineBase(BaseModel):
    message: str = None
    customer: Customer = None


class TimelineBaseInDB(TimelineBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class TimelineInCreate(TimelineBase):
    pass


# Properties to receive via API on update
class TimelineInUpdate(TimelineBase):
    pass


# Additional properties to return via API
class Timeline(TimelineBaseInDB):
    pass


# Additional properties stored in DB
class TimelineInDB(TimelineBaseInDB):
    pass
