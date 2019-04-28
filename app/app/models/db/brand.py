from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.models.db import Base


class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    devices = relationship("Device", back_populates='brand')
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
