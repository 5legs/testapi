from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
from app.models.db import Base


class DeviceVRF(Base):
    __tablename__ = "device_vrf"
    device_id = Column(Integer, ForeignKey("device.id"), primary_key=True)
    vrf_id = Column(Integer, ForeignKey("vrf.id"), primary_key=True)
