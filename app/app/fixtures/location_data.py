from app.models.location import LocationInCreate
from app.crud.location import get_by_name, create
from app.db.session import db_session


def init_location_data():
    location = get_by_name(db_session, name="Y1")
    if not location:
        location_in = LocationInCreate(name="Y1", address="FrankFurt")
        location = create(db_session, location_in=location_in)

    location = get_by_name(db_session, name="Z2")
    if not location:
        location_in = LocationInCreate(name="Z2", address="Ronchin")
        location = create(db_session, location_in=location_in)

    location = get_by_name(db_session, name="N1")
    if not location:
        location_in = LocationInCreate(name="N1", address="FrankFurt")
        location = create(db_session, location_in=location_in)

    location = get_by_name(db_session, name="N2")
    if not location:
        location_in = LocationInCreate(name="N2", address="Paris")
        location = create(db_session, location_in=location_in)

    location = get_by_name(db_session, name="I2")
    if not location:
        location_in = LocationInCreate(name="I2", address="Seclin")
        location = create(db_session, location_in=location_in)
