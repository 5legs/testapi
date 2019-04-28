from typing import List
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_406_NOT_ACCEPTABLE,
)
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.autonomous import (
    Autonomous,
    AutonomousInCreate,
    AutonomousInUpdate,
)
from app.api.utils.security import check_token
from app.crud.autonomous import (
    get,
    get_multi,
    get_by_number,
    create,
    delete,
    update,
)

Tags = ["Autonomous"]

router = APIRouter()


@router.get(
    "/{autonomous_id}",
    tags=Tags,
    status_code=HTTP_200_OK,
    response_model=Autonomous,
)
def read_autonomous(
    autonomous_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    if authorized:
        autonomous = get(db, autonomous_id=autonomous_id)
        if not autonomous:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Autonomous System does not exist",
            )
        return autonomous


@router.get(
    "/", tags=Tags, status_code=HTTP_200_OK, response_model=List[Autonomous]
)
def read_multiple_autonomous(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve autonomous
    """
    if authorized:
        Lautonomous = get_multi(db, skip=skip, limit=limit)
        return Lautonomous


@router.post(
    "/", tags=Tags, status_code=HTTP_201_CREATED, response_model=Autonomous
)
def create_autonomous(
    *,
    db: Session = Depends(get_db),
    autonomous_in: AutonomousInCreate,
    authorized: bool = Depends(check_token)
):
    """
    Create new autonomous
    """
    if authorized:
        autonomous = get_by_number(db, number=autonomous_in.number)
        if autonomous:
            raise HTTPException(
                status_code=HTTP_406_NOT_ACCEPTABLE,
                detail="Autonomous System already exists.",
            )
        autonomous = create(db, autonomous_in=autonomous_in)
        return autonomous


@router.put(
    "/{autonomous_id}",
    tags=Tags,
    status_code=HTTP_200_OK,
    response_model=Autonomous,
)
def update_autonomous(
    *,
    db: Session = Depends(get_db),
    autonomous_id: int,
    autonomous_in: AutonomousInUpdate,
    authorized: bool = Depends(check_token)
):
    """
    Update a autonomous
    """
    if authorized:
        autonomous = get(db, autonomous_id=autonomous_id)

        if not autonomous:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Autonomous System does not exist",
            )
        autonomous = update(
            db, autonomous=autonomous, autonomous_in=autonomous_in
        )
        return autonomous


@router.delete(
    "/{autonomous_id}", tags=Tags, status_code=HTTP_200_OK, response_model=bool
)
def delete_autonomous(
    autonomous_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    """
    delete autonomous
    """
    if authorized:
        autonomous = get(db, autonomous_id=autonomous_id)
        if not autonomous:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Autonomous System does not exist.",
            )
        if delete(db, autonomous_id=autonomous_id):
            return True
        return False
