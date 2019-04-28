from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.brand import Brand, BrandInCreate, BrandInUpdate
from app.api.utils.security import check_token
from app.crud.brand import get, get_multi, get_by_name, create, delete, update

Tags = ["Brand"]

router = APIRouter()


@router.get("/{brand_id}", tags=Tags, response_model=Brand)
def read_brand(
    brand_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    if authorized:
        brand = get(db, brand_id=brand_id)
        if not brand:
            raise HTTPException(status_code=404, detail="Brand does not exist")
        return brand


@router.get("/", tags=Tags, response_model=List[Brand])
def read_brands(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve brands
    """
    if authorized:
        brands = get_multi(db, skip=skip, limit=limit)
        return brands


@router.post("/", tags=Tags, response_model=Brand)
def create_brand(
    *,
    db: Session = Depends(get_db),
    brand_in: BrandInCreate,
    authorized: bool = Depends(check_token)
):
    """
    Create new brand
    """
    if authorized:
        brand = get_by_name(db, name=brand_in.name)
        if brand:
            raise HTTPException(
                status_code=400, detail="The brand already exists."
            )
        brand = create(db, brand_in=brand_in)
        return brand


@router.put("/{brand_id}", tags=Tags, response_model=Brand)
def update_brand(
    *,
    db: Session = Depends(get_db),
    brand_id: int,
    brand_in: BrandInUpdate,
    authorized: bool = Depends(check_token)
):
    """
    Update a brand
    """
    if authorized:
        brand = get(db, brand_id=brand_id)

        if not brand:
            raise HTTPException(status_code=404, detail="Brand does not exist")
        brand = update(db, brand=brand, brand_in=brand_in)
        return brand


@router.delete("/{brand_id}", tags=Tags, response_model=bool)
def delete_brand(
    brand_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    """
    delete brand
    """
    if authorized:
        brand = get(db, brand_id=brand_id)
        if not brand:
            raise HTTPException(
                status_code=400, detail="The brand does not exist."
            )
        if delete(db, brand_id=brand_id):
            return True
        return False
