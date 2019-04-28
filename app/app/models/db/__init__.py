from sqlalchemy.ext.declarative import declarative_base, declared_attr
from app.db.session import engine
from app.api.utils.logging import logger


class CustomBase(object):
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)


from .customer import Customer
from .device import Device
from .vrf import VRF
from .device_vrf import DeviceVRF
from .customer_device import CustomerDevice
from .brand import Brand
from .autonomous import Autonomous
from .interface import Interface
from .location import Location
from .timeline import Timeline


logger.info("Creating database")
Base.metadata.create_all(engine)


from app.fixtures.location_data import init_location_data

logger.info("Populate location")
init_location_data()


from app.fixtures.brand_data import init_brand_data

logger.info("Populate brand")
init_brand_data()


from app.fixtures.vrf_data import init_vrf_data

logger.info("Populate VRF")
init_vrf_data()


from app.fixtures.device_data import init_device_data

logger.info("Populate Device")
init_device_data()
