from app.models.brand import BrandInCreate
from app.crud.brand import get_by_name, create
from app.db.session import db_session


def init_brand_data():
    brand = get_by_name(db_session, name="Cisco")
    if not brand:
        brand_in = BrandInCreate(name="Cisco")
        brand = create(db_session, brand_in=brand_in)

    brand = get_by_name(db_session, name="Stonesoft")
    if not brand:
        brand_in = BrandInCreate(name="Stonesoft")
        brand = create(db_session, brand_in=brand_in)

    brand = get_by_name(db_session, name="Palo alto")
    if not brand:
        brand_in = BrandInCreate(name="Palo alto")
        brand = create(db_session, brand_in=brand_in)
