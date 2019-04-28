from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.device import Device as DBDevice
from app.models.db.brand import Brand as DBBrand
from app.models.db.location import Location as DBLocation
from app.models.brand import BrandInCreate
from app.crud.brand import (
    get_by_name as get_brand_by_name,
    create as createbrand,
)
from app.models.location import LocationInCreate
from app.crud.location import (
    get_by_name as get_location_by_name,
    create as createlocation,
)
from app.models.device import DeviceInCreate, DeviceInUpdate, Device

import datetime


def get(db_session, *, device_id: int) -> Device:
    return db_session.query(DBDevice).join(DBBrand).join(DBLocation).filter(DBDevice.id == device_id).first()


def get_by_name(db_session, *, name: str) -> Optional[Device]:
    return db_session.query(DBDevice).join(DBBrand).join(DBLocation).filter(DBDevice.name == name).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Device]]:
    return db_session.query(DBDevice).join(DBBrand).join(DBLocation).offset(skip).limit(limit).all()


def create(db_session, *, device_in: DeviceInCreate) -> Device:
    brand = get_brand_by_name(db_session, name=device_in.brand.name)
    if not brand:
        brand_in = BrandInCreate(name=device_in.brand.name)
        brand = createbrand(db_session, brand_in=brand_in)

    location = get_location_by_name(db_session, name=device_in.location.name)
    if not location:
        location_in = LocationInCreate(name=device_in.location.name)
        location = createlocation(db_session, location_in=location_in)

    device = DBDevice(
        fqdn=device_in.fqdn,
        name=device_in.name,
        brand=brand,
        role=device_in.role,
        type=device_in.type,
        serial=device_in.serial,
        version=device_in.version,
        location=location
    )
    db_session.add(device)
    db_session.commit()
    db_session.refresh(device)
    return device


def update(
    db_session, *, device: DBDevice, device_in: DeviceInUpdate
) -> Device:
    device_data = jsonable_encoder(device)
    for field in device_data:
        if field in device_in.fields:
            value_in = getattr(device_in, field)
            if value_in is not None:
                setattr(device, field, value_in)
    device.updated_at = str(datetime.datetime.now())
    db_session.add(device)
    db_session.commit()
    db_session.refresh(device)
    return device


def delete(db_session, *, device_id: int) -> bool:
    device = get(db_session, device_id=device_id)
    if device:
        db_session.delete(device)
        db_session.commit()
        return True
    return False
