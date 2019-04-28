from app import crud
from app.db.session import db_session
from app.models.brand import BrandInCreate
from app.tests.utils.utils import random_lower_string

global name
name = random_lower_string()


def test_create_brand():
    """
    create a brand
    """
    brand_in = BrandInCreate(name=name)
    brand = crud.brand.create(db_session, brand_in=brand_in)
    assert brand.name == name.upper()


def test_get_brand():
    """
    get a brand
    """
    brand = crud.brand.get_by_name(db_session, name=name)
    assert brand.name
