from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.location import Location, LocationInCreate, LocationInUpdate
from app.api.utils.security import check_token
from app.crud.location import (
    get,
    get_multi,
    get_by_name,
    create,
    delete,
    update,
)

Tags = ["Location"]

router = APIRouter()


@router.get("/{location_id}", tags=Tags, response_model=Location)
def read_location(
    location_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    if authorized:
        location = get(db, location_id=location_id)
        if not location:
            raise HTTPException(
                status_code=404, detail="Location does not exist"
            )
        return location


@router.get("/", tags=Tags, response_model=List[Location])
def read_locations(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve locations
    """
    if authorized:
        locations = get_multi(db, skip=skip, limit=limit)
        return locations


@router.post("/", tags=Tags, response_model=Location)
def create_location(
    *,
    db: Session = Depends(get_db),
    location_in: LocationInCreate,
    authorized: bool = Depends(check_token)
):
    """
    Create new location
    """
    if authorized:
        location = get_by_name(db, name=location_in.name)
        if location:
            raise HTTPException(
                status_code=400, detail="The location already exists."
            )
        location = create(db, location_in=location_in)
        return location


@router.put("/{location_id}", tags=Tags, response_model=Location)
def update_location(
    *,
    db: Session = Depends(get_db),
    location_id: int,
    location_in: LocationInUpdate,
    authorized: bool = Depends(check_token)
):
    """
    Update a location
    """
    if authorized:
        location = get(db, location_id=location_id)

        if not location:
            raise HTTPException(
                status_code=404, detail="Location does not exist"
            )
        location = update(db, location=location, location_in=location_in)
        return location


@router.delete("/{location_id}", tags=Tags, response_model=bool)
def delete_location(
    location_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    """
    delete location
    """
    if authorized:
        location = get(db, location_id=location_id)
        if not location:
            raise HTTPException(
                status_code=400, detail="The location does not exist."
            )
        if delete(db, location_id=location_id):
            return True
        return False
