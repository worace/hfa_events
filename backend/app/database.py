from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

class DB(object):
    def __init__(self, db_name):
        self.engine = create_engine('postgresql:///%s' % db_name)

    def connect(self):
        self.connection = self.engine.connect()
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=self.engine))
    def query(self, model_cls):
        return self.session.query(model_cls)

    def disconnect(self):
        self.session.close()
        self.connection.close()

    def init_db(self):
        self.connect()
        import app.models
        Model.metadata.create_all(bind = self.engine)

    def save_records(self, *records):
        try:
            for r in records:
                self.session.add(r)
            return self.session.commit()
        except Exception, e:
            self.session.rollback()
            raise e

