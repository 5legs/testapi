from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.brand import Brand as DBBrand
from app.models.brand import BrandInCreate, BrandInUpdate, Brand

import datetime


def get(db_session, *, brand_id: int) -> Brand:
    return db_session.query(DBBrand).filter(DBBrand.id == brand_id).first()


def get_by_name(db_session, *, name: str) -> Optional[Brand]:
    return db_session.query(DBBrand).filter(DBBrand.name == name).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Brand]]:
    return db_session.query(DBBrand).offset(skip).limit(limit).all()


def create(db_session, *, brand_in: BrandInCreate) -> Brand:
    brand = DBBrand(name=brand_in.name)
    db_session.add(brand)
    db_session.commit()
    db_session.refresh(brand)
    return brand


def update(db_session, *, brand: DBBrand, brand_in: BrandInUpdate) -> Brand:
    brand_data = jsonable_encoder(brand)
    for field in brand_data:
        if field in brand_in.fields:
            value_in = getattr(brand_in, field)
            if value_in is not None:
                setattr(brand, field, value_in)
    brand.updated_at = str(datetime.datetime.now())
    db_session.add(brand)
    db_session.commit()
    db_session.refresh(brand)
    return brand


def delete(db_session, *, brand_id: int) -> bool:
    brand = get(db_session, brand_id=brand_id)
    if brand:
        db_session.delete(brand)
        db_session.commit()
        return True
    return False
