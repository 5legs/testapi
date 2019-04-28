from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.models.db import Base


class Interface(Base):
    __tablename__ = "interface"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    vrf_id = Column(Integer, ForeignKey("vrf.id"))
    vrf = relationship("VRF", backref="vrf")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
