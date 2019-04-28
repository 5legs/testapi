from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import datetime
from app.models.db import Base
from app.models.role import RoleEnum
from app.models.type import TypeEnum


class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, index=True)
    fqdn = Column(String, index=True)
    name = Column(String, unique=True, index=True)
    role = Column(Enum(RoleEnum), nullable=False)
    type = Column(Enum(TypeEnum), nullable=False)
    brand_id = Column(Integer, ForeignKey("brand.id"))
    brand = relationship("Brand", back_populates="devices")
    location_id = Column(Integer, ForeignKey("location.id"))
    location = relationship("Location", back_populates="devices")
    serial = Column(String, unique=True)
    version = Column(String)
    management_ip = Column(String, unique=True)
    vrfs = relationship("VRF", secondary="device_vrf", back_populates="devices")
    customers = relationship("CustomerDevice", back_populates="device")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
