from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from ipaddress import IPv4Network


# Shared properties
class NetworkBase(BaseModel):
    ipv4: IPv4Network = None


class NetworkBaseInDB(NetworkBase):
    id: int = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Properties to receive via API on creation
class NetworkInCreate(NetworkBase):
    pass


# Properties to receive via API on update
class NetworkInUpdate(NetworkBaseInDB):
    pass


# Additional properties to return via API
class Network(NetworkBaseInDB):
    pass


# Additional properties stored in DB
class NetworkInDB(NetworkBaseInDB):
    pass
