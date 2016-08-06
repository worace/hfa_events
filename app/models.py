from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Model

class Event(Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    locations = relationship("Location", back_populates="event")

    def __repr__(self):
        return "<Event id: %s, name: %s>" % (self.id, self.name)

class Location(Model):
    __tablename__ = "locations"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="locations")

    def __repr__(self):
        return "<Location id: %s, name: %s, event_id: %s>" % (self.id, self.name, self.event_id)
