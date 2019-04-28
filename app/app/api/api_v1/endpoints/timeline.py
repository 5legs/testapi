from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.timeline import Timeline, TimelineInCreate, TimelineInUpdate
from app.api.utils.security import check_token
from app.crud.timeline import (
    get,
    get_multi,
    get_by_name,
    create,
    delete,
    update,
)

Tags = ["Timeline"]

router = APIRouter()


@router.get("/{timeline_id}", tags=Tags, response_model=Timeline)
def read_timeline(
    timeline_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    if authorized:
        timeline = get(db, timeline_id=timeline_id)
        if not timeline:
            raise HTTPException(
                status_code=404, detail="Timeline does not exist"
            )
        return timeline


@router.get("/", tags=Tags, response_model=List[Timeline])
def read_timelines(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve timelines
    """
    if authorized:
        timelines = get_multi(db, skip=skip, limit=limit)
        return timelines


@router.post("/", tags=Tags, response_model=Timeline)
def create_timeline(
    *,
    db: Session = Depends(get_db),
    timeline_in: TimelineInCreate,
    authorized: bool = Depends(check_token)
):
    """
    Create new timeline
    """
    if authorized:
        timeline = get_by_name(db, name=timeline_in.name)
        if timeline:
            raise HTTPException(
                status_code=400, detail="The timeline already exists."
            )
        timeline = create(db, timeline_in=timeline_in)
        return timeline


@router.put("/{timeline_id}", tags=Tags, response_model=Timeline)
def update_timeline(
    *,
    db: Session = Depends(get_db),
    timeline_id: int,
    timeline_in: TimelineInUpdate,
    authorized: bool = Depends(check_token)
):
    """
    Update a timeline
    """
    if authorized:
        timeline = get(db, timeline_id=timeline_id)

        if not timeline:
            raise HTTPException(
                status_code=404, detail="Timeline does not exist"
            )
        timeline = update(db, timeline=timeline, timeline_in=timeline_in)
        return timeline


@router.delete("/{timeline_id}", tags=Tags, response_model=bool)
def delete_timeline(
    timeline_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    """
    delete timeline
    """
    if authorized:
        timeline = get(db, timeline_id=timeline_id)
        if not timeline:
            raise HTTPException(
                status_code=400, detail="The timeline does not exist."
            )
        if delete(db, timeline_id=timeline_id):
            return True
        return False
