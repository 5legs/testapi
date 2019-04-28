from typing import Optional
from datetime import datetime
from pydantic import BaseModel, constr


# Shared properties
class AutonomousBase(BaseModel):
    number: constr(
        regex=r"^([1-5]\d{4}|[1-9]\d{0,3}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])(\.([1-5]\d{4}|[1-9]\d{0,3}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5]|0))?$"
    ) = None


class AutonomousBaseInDB(AutonomousBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class AutonomousInCreate(AutonomousBase):
    pass


# Properties to receive via API on update
class AutonomousInUpdate(AutonomousBase):
    pass


# Additional properties to return via API
class Autonomous(AutonomousBaseInDB):
    pass


# Additional properties stored in DB
class AutonomousInDB(AutonomousBaseInDB):
    pass
