from app.models.vrf import VRFInCreate
from app.crud.vrf import get_by_name, create
from app.db.session import db_session


def init_vrf_data():
    vrf = get_by_name(db_session, name="WAN_ITBM")
    if not vrf:
        vrf_in = VRFInCreate(name="WAN_ITBM")
        vrf = create(db_session, vrf_in=vrf_in)

    vrf = get_by_name(db_session, name="WAN_ITLM")
    if not vrf:
        vrf_in = VRFInCreate(name="WAN_ITLM")
        vrf = create(db_session, vrf_in=vrf_in)

    vrf = get_by_name(db_session, name="WAN_ITBC")
    if not vrf:
        vrf_in = VRFInCreate(name="WAN_ITBC")
        vrf = create(db_session, vrf_in=vrf_in)

    vrf = get_by_name(db_session, name="WAN_ITZD")
    if not vrf:
        vrf_in = VRFInCreate(name="WAN_ITZD")
        vrf = create(db_session, vrf_in=vrf_in)

    vrf = get_by_name(db_session, name="WAN_FRBM")
    if not vrf:
        vrf_in = VRFInCreate(name="WAN_FRBM")
        vrf = create(db_session, vrf_in=vrf_in)
