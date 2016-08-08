from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Model
from sqlalchemy import desc
from app.models.shared import Serializable

class Attendee(Model, Serializable):
    __tablename__ = "attendees"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="attendees")

    def serialized_attrs(self):
        return ["name", "email"]

