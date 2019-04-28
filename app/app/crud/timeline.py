from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.timeline import Timeline as DBTimeline
from app.models.timeline import TimelineInCreate, TimelineInUpdate, Timeline

import datetime


def get(db_session, *, timeline_id: int) -> Timeline:
    return (
        db_session.query(DBTimeline)
        .filter(DBTimeline.id == timeline_id)
        .first()
    )


def get_by_name(db_session, *, name: str) -> Optional[Timeline]:
    return db_session.query(DBTimeline).filter(DBTimeline.name == name).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Timeline]]:
    return db_session.query(DBTimeline).offset(skip).limit(limit).all()


def create(db_session, *, timeline_in: TimelineInCreate) -> Timeline:
    timeline = DBTimeline(name=timeline_in.name)
    db_session.add(timeline)
    db_session.commit()
    db_session.refresh(timeline)
    return timeline


def update(
    db_session, *, timeline: DBTimeline, timeline_in: TimelineInUpdate
) -> Timeline:
    timeline_data = jsonable_encoder(timeline)
    for field in timeline_data:
        if field in timeline_in.fields:
            value_in = getattr(timeline_in, field)
            if value_in is not None:
                setattr(timeline, field, value_in)
    timeline.updated_at = str(datetime.datetime.now())
    db_session.add(timeline)
    db_session.commit()
    db_session.refresh(timeline)
    return timeline


def delete(db_session, *, timeline_id: int) -> bool:
    timeline = get(db_session, timeline_id=timeline_id)
    if timeline:
        db_session.delete(timeline)
        db_session.commit()
        return True
    return False
