from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.customer import Customer, CustomerInCreate, CustomerInUpdate
from app.api.utils.security import check_token
from app.crud.customer import (
    get,
    get_multi,
    get_by_name,
    create,
    delete,
    update,
)

Tags = ["Customer"]

router = APIRouter()


@router.get("/{customer_id}", tags=Tags, response_model=Customer)
def read_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    if authorized:
        customer = get(db, customer_id=customer_id)
        return customer


@router.get("/", tags=Tags, response_model=List[Customer])
def read_customers(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve customers
    """
    if authorized:
        customers = get_multi(db, skip=skip, limit=limit)
        return customers


@router.post("/", tags=Tags, response_model=Customer)
def create_customer(
    *,
    db: Session = Depends(get_db),
    customer_in: CustomerInCreate,
    authorized: bool = Depends(check_token)
):
    """
    Create new customer
    """
    if authorized:
        customer = get_by_name(db, name=customer_in.name)
        if customer:
            raise HTTPException(
                status_code=400, detail="The customer already exists."
            )
        customer = create(db, customer_in=customer_in)
        return customer


@router.put("/{customer_id}", tags=Tags, response_model=Customer)
def update_customer(
    *,
    db: Session = Depends(get_db),
    customer_id: int,
    customer_in: CustomerInUpdate,
    authorized: bool = Depends(check_token)
):
    """
    Update a customer
    """
    if authorized:
        customer = get(db, customer_id=customer_id)

        if not customer:
            raise HTTPException(
                status_code=404, detail="Customer does not exist"
            )
        customer = update(db, customer=customer, customer_in=customer_in)
        return customer


@router.delete("/{customer_id}", tags=Tags, response_model=bool)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    """
    delete customer
    """
    if authorized:
        customer = get(db, customer_id=customer_id)
        if not customer:
            raise HTTPException(
                status_code=400, detail="The customer does not exist."
            )
        if delete(db, customer_id=customer_id):
            return True
        return False
