from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Model
from sqlalchemy import desc
from app.models.shared import Serializable, Pageable, ascii_keys

class Event(Model, Serializable, Pageable):
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
    attendees = relationship("Attendee", back_populates="event")

    @classmethod
    def default_order(cls):
        return desc(Event.start_date)

    def __init__(self, **attributes):
        encoded = ascii_keys(attributes)
        super(Event, self).__init__(**attributes)

    def __repr__(self):
        return "<Event id: %s, name: %s>" % (self.id, self.name)

    @property
    def attendee_info(self):
        return map(lambda att: att.serialize(), self.attendees)

    @property
    def location_info(self):
        if self.locations:
            return self.locations[0].serialize()
        else:
            return None

    def serialized_attrs(self):
        return ["id", "name", "start_date", "end_date","description",
                "status", "location_info", "attendee_info"]
