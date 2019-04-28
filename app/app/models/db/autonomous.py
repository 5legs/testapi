from sqlalchemy import Column, Integer, String, DateTime
import datetime
from app.models.db import Base


class Autonomous(Base):
    __tablename__ = "autonomous"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
