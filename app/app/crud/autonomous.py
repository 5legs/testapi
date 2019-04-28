from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.autonomous import Autonomous as DBAutonomous
from app.models.autonomous import (
    AutonomousInCreate,
    AutonomousInUpdate,
    Autonomous,
)

import datetime


def get(db_session, *, autonomous_id: int) -> Autonomous:
    return (
        db_session.query(DBAutonomous)
        .filter(DBAutonomous.id == autonomous_id)
        .first()
    )


def get_by_number(db_session, *, number: str) -> Optional[Autonomous]:
    return (
        db_session.query(DBAutonomous)
        .filter(DBAutonomous.number == number)
        .first()
    )


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Autonomous]]:
    return db_session.query(DBAutonomous).offset(skip).limit(limit).all()


def create(db_session, *, autonomous_in: AutonomousInCreate) -> Autonomous:
    autonomous = DBAutonomous(number=autonomous_in.number)
    db_session.add(autonomous)
    db_session.commit()
    db_session.refresh(autonomous)
    return autonomous


def update(
    db_session, *, autonomous: DBAutonomous, autonomous_in: AutonomousInUpdate
) -> Autonomous:
    autonomous_data = jsonable_encoder(autonomous)
    for field in autonomous_data:
        if field in autonomous_in.fields:
            value_in = getattr(autonomous_in, field)
            if value_in is not None:
                setattr(autonomous, field, value_in)
    autonomous.updated_at = str(datetime.datetime.now())
    db_session.add(autonomous)
    db_session.commit()
    db_session.refresh(autonomous)
    return autonomous


def delete(db_session, *, autonomous_id: int) -> bool:
    autonomous = get(db_session, autonomous_id=autonomous_id)
    if autonomous:
        db_session.delete(autonomous)
        db_session.commit()
        return True
    return False
