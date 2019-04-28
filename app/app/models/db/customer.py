from sqlalchemy import Boolean, Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
import datetime
from app.models.db import Base
from app.models.customer_type import CustomerTypeEnum


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    galaxis_bu_id = Column(Integer, unique=True, nullable=False)
    # autonomous = relationship("Autonomous")
    type = Column(Enum(CustomerTypeEnum), nullable=False)
    devices = relationship("CustomerDevice", back_populates="customer")
    enabled = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
