from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, validator, constr
from app.models.customer_type import CustomerTypeEnum
from app.models.device import Device


# Shared properties
class CustomerBase(BaseModel):
    name: constr(regex=r"^([a-zA-Z]{4})$")
    full_name: Optional[constr(regex=r"^([a-zA-Z\ ]*)$")]
    type: CustomerTypeEnum = CustomerTypeEnum.customer
    galaxis_bu_id: Optional[int] = None
    enabled: Optional[bool] = True

    @validator("name")
    def transform_name(cls, v):
        return v.upper()

    @validator("full_name")
    def transform_full_name(cls, v):
        return v.title()


class CustomerBaseInDB(CustomerBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class CustomerInCreate(CustomerBase):
    pass


# Properties to receive via API on update
class CustomerInUpdate(CustomerBase):
    pass


# Additional properties to return via API
class Customer(CustomerBaseInDB):
    # autonomous : Optional[Autonomous] = None
    device: Optional[List[Device]] = None


# Additional properties stored in DB
class CustomerInDB(CustomerBaseInDB):
    pass
