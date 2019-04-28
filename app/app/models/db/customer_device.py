from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.db import Base


class CustomerDevice(Base):
    __tablename__ = "customer_device"
    customer_id = Column(Integer, ForeignKey("customer.id"), primary_key=True)
    device_id = Column(Integer, ForeignKey("device.id"), primary_key=True)
    customer = relationship("Customer", back_populates="devices")
    device = relationship("Device", back_populates="customers")
