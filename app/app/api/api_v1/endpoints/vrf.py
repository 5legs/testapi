from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.vrf import VRF, VRFInCreate, VRFInUpdate
from app.api.utils.security import check_token
from app.crud.vrf import get, get_multi, get_by_name, create, delete, update

Tags = ["VRF"]

router = APIRouter()


@router.get("/{vrf_id}", tags=Tags, response_model=VRF)
def read_vrf(
    vrf_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    if authorized:
        vrf = get(db, vrf_id=vrf_id)
        if not vrf:
            raise HTTPException(status_code=404, detail="VRF does not exist")
        return vrf


@router.get("/", tags=Tags, response_model=List[VRF])
def read_vrfs(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve vrfs
    """
    if authorized:
        vrfs = get_multi(db, skip=skip, limit=limit)
        return vrfs


@router.post("/", tags=Tags, response_model=VRF)
def create_vrf(
    *,
    db: Session = Depends(get_db),
    vrf_in: VRFInCreate,
    authorized: bool = Depends(check_token)
):
    """
    Create new vrf
    """
    if authorized:
        vrf = get_by_name(db, name=vrf_in.name)
        if vrf:
            raise HTTPException(
                status_code=400, detail="The vrf already exists."
            )
        vrf = create(db, vrf_in=vrf_in)
        return vrf


@router.put("/{vrf_id}", tags=Tags, response_model=VRF)
def update_vrf(
    *,
    db: Session = Depends(get_db),
    vrf_id: int,
    vrf_in: VRFInUpdate,
    authorized: bool = Depends(check_token)
):
    """
    Update a vrf
    """
    if authorized:
        vrf = get(db, vrf_id=vrf_id)

        if not vrf:
            raise HTTPException(status_code=404, detail="VRF does not exist")
        vrf = update(db, vrf=vrf, vrf_in=vrf_in)
        return vrf


@router.delete("/{vrf_id}", tags=Tags, response_model=bool)
def delete_vrf(
    vrf_id: int,
    db: Session = Depends(get_db),
    authorized: bool = Depends(check_token),
):
    """
    delete vrf
    """
    if authorized:
        vrf = get(db, vrf_id=vrf_id)
        if not vrf:
            raise HTTPException(
                status_code=400, detail="The vrf does not exist."
            )
        if delete(db, vrf_id=vrf_id):
            return True
        return False
