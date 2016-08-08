from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Model
from sqlalchemy import desc

def ascii_keys(d):
    return dict(map(lambda (k,v): (k.encode("ascii"), v),
                    d.items()))

class Serializable(object):
    def serialized_attrs(self):
        return []

    def serialize(self):
        attrs = {}
        for attr in self.serialized_attrs():
            attrs[attr] = getattr(self, attr)

        return attrs

class Pageable(object):
    @classmethod
    def default_order(cls):
        return cls.id

    @classmethod
    def paged(cls, db, page = 1, limit = 10, options = []):
        return (db.session
                .query(cls)
                .options(*options)
                .order_by(cls.default_order())
                .limit(limit)
                .offset((page - 1) * limit)
                .all())

    @classmethod
    def create(cls, db, **attributes):
        event = cls(**attributes)
        db.save_records(event)
