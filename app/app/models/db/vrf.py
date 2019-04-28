from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.models.db import Base


class VRF(Base):
    __tablename__ = "vrf"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    interface = relationship("Interface")
    # autonomous = relationship(Autonomous)
    devices = relationship("Device", secondary="device_vrf", back_populates="vrfs")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
