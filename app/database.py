from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

class DB(object):
    def __init__(self, db_name):
        self.engine = create_engine('postgresql:///%s' % db_name)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=self.engine))

    def init_db(self):
        import app.models
        Model.metadata.create_all(bind = self.engine)
