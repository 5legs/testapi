from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.vrf import VRF as DBVRF
from app.models.vrf import VRFInCreate, VRFInUpdate, VRF

import datetime


def get(db_session, *, vrf_id: int) -> VRF:
    return db_session.query(DBVRF).filter(DBVRF.id == vrf_id).first()


def get_by_name(db_session, *, name: str) -> Optional[VRF]:
    return db_session.query(DBVRF).filter(DBVRF.name == name).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[VRF]]:
    return db_session.query(DBVRF).offset(skip).limit(limit).all()


def create(db_session, *, vrf_in: VRFInCreate) -> VRF:
    vrf = DBVRF(name=vrf_in.name)
    db_session.add(vrf)
    db_session.commit()
    db_session.refresh(vrf)
    return vrf


def update(db_session, *, vrf: DBVRF, vrf_in: VRFInUpdate) -> VRF:
    vrf_data = jsonable_encoder(vrf)
    for field in vrf_data:
        if field in vrf_in.fields:
            value_in = getattr(vrf_in, field)
            if value_in is not None:
                setattr(vrf, field, value_in)
    vrf.updated_at = str(datetime.datetime.now())
    db_session.add(vrf)
    db_session.commit()
    db_session.refresh(vrf)
    return vrf


def delete(db_session, *, vrf_id: int) -> bool:
    vrf = get(db_session, vrf_id=vrf_id)
    if vrf:
        db_session.delete(vrf)
        db_session.commit()
        return True
    return False
