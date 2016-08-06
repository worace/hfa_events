from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Model

def ascii_keys(d):
    return dict(map(lambda (k,v): (k.encode("ascii"), v),
                    d.items()))

class Event(Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    status = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    description = Column(String)
    official = Column(Boolean)
    visibility = Column(String)
    guests_can_invite_others = Column(Boolean)
    modified_date = Column(DateTime)
    created_date = Column(DateTime)
    participant_count = Column(Integer)
    reason_for_private = Column(String)
    order_email_template = Column(String)
    locations = relationship("Location", back_populates="event")

    def __init__(self, **attributes):
        encoded = ascii_keys(attributes)
        super(Event, self).__init__(**attributes)

    def __repr__(self):
        return "<Event id: %s, name: %s>" % (self.id, self.name)

    def serialize(self):
        return {"id": self.id, "name": self.name}

class Location(Model):
    __tablename__ = "locations"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="locations")

    def __repr__(self):
        return "<Location id: %s, name: %s, event_id: %s>" % (self.id, self.name, self.event_id)
