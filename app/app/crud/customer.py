from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.customer import Customer as DBCustomer
from app.models.customer import CustomerInCreate, CustomerInUpdate, Customer
import datetime


def get(db_session, *, customer_id: int) -> Customer:
    return (
        db_session.query(DBCustomer)
        .filter(DBCustomer.id == customer_id)
        .first()
    )


def get_by_name(db_session, *, name: str) -> Optional[Customer]:
    return db_session.query(DBCustomer).filter(DBCustomer.name == name).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Customer]]:
    return db_session.query(DBCustomer).offset(skip).limit(limit).all()


def create(db_session, *, customer_in: CustomerInCreate) -> Customer:
    customer = DBCustomer(
        name=customer_in.name,
        full_name=customer_in.full_name,
        galaxis_bu_id=customer_in.galaxis_bu_id,
        enabled=customer_in.enabled,
        type=customer_in.type,
    )
    db_session.add(customer)
    db_session.commit()
    db_session.refresh(customer)
    return customer


def update(
    db_session, *, customer: DBCustomer, customer_in: CustomerInUpdate
) -> Customer:
    customer_data = jsonable_encoder(customer)
    for field in customer_data:
        if field in customer_in.fields:
            value_in = getattr(customer_in, field)
            if value_in is not None:
                setattr(customer, field, value_in)
    customer.updated_at = str(datetime.datetime.now())
    db_session.add(customer)
    db_session.commit()
    db_session.refresh(customer)
    return customer


def delete(db_session, *, customer_id: int) -> bool:
    customer = get(db_session, customer_id=customer_id)
    if customer:
        db_session.delete(customer)
        db_session.commit()
        return True
    return False
