from app.models.device import DeviceInCreate
from app.crud.device import get_by_name as get_device_by_name, create as create_device
from app.crud.brand import get_by_name as get_brand_by_name, create as create_brand
from app.crud.location import get_by_name as get_location_by_name, create as create_location
from app.db.session import db_session


def init_device_data():
    device = get_device_by_name(db_session, name="phmbun1corea")
    if not device:
        brand = get_brand_by_name(db_session, name="Cisco")
        location = get_location_by_name(db_session, name="Y1")
        device_in = DeviceInCreate(
            name="phmbun1corea",
            fqdn=f"phmbun1corea.int.adeo.com",
            brand={'name': brand.name},
            role="netcenter",
            type="router",
            serial="",
            version="",
            location={'name': location.name},
        )
        device = create_device(db_session, device_in=device_in)
