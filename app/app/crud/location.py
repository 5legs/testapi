from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.location import Location as DBLocation
from app.models.location import LocationInCreate, LocationInUpdate, Location

import datetime


def get(db_session, *, location_id: int) -> Location:
    return (
        db_session.query(DBLocation)
        .filter(DBLocation.id == location_id)
        .first()
    )


def get_by_name(db_session, *, name: str) -> Optional[Location]:
    return db_session.query(DBLocation).filter(DBLocation.name == name).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Location]]:
    return db_session.query(DBLocation).offset(skip).limit(limit).all()


def create(db_session, *, location_in: LocationInCreate) -> Location:
    location = DBLocation(name=location_in.name, address=location_in.address)
    db_session.add(location)
    db_session.commit()
    db_session.refresh(location)
    return location


def update(
    db_session, *, location: DBLocation, location_in: LocationInUpdate
) -> Location:
    location_data = jsonable_encoder(location)
    for field in location_data:
        if field in location_in.fields:
            value_in = getattr(location_in, field)
            if value_in is not None:
                setattr(location, field, value_in)
    location.updated_at = str(datetime.datetime.now())
    db_session.add(location)
    db_session.commit()
    db_session.refresh(location)
    return location


def delete(db_session, *, location_id: int) -> bool:
    location = get(db_session, location_id=location_id)
    if location:
        db_session.delete(location)
        db_session.commit()
        return True
    return False
