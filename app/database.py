from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql:///hfa_events')
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Model = declarative_base()
# Base.query = db_session.query_property()

def init_db():
    import app.models
    Model.metadata.create_all(bind = engine)
