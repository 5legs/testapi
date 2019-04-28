# from app.db.base_class import Base,engine
# from app.models.db import *
# from app.api.utils.logging import logger
# from app.fixtures import location_data

# __all__ = ['Customer','Device','CustomerDevice','Brand','Autonomous','Interface','Location','Timeline','VRF']

# def init_db():
#     logger.info("Creating the db")
#     Base.metadata.create_all(bind=engine)

#     logger.info("Population Location")
#     location_data.init_location_data()
