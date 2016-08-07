from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Model

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

class Attendee(Model, Serializable):
    __tablename__ = "attendees"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="attendees")

class Event(Model, Serializable):
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

    def __init__(self, **attributes):
        encoded = ascii_keys(attributes)
        super(Event, self).__init__(**attributes)

    def __repr__(self):
        return "<Event id: %s, name: %s>" % (self.id, self.name)

    @property
    def location_info(self):
        if self.locations:
            return self.locations[0].serialize()
        else:
            return None

    def serialized_attrs(self):
        return ["id", "name", "start_date", "end_date","description",
                "participant_count", "status", "location_info"]

class Location(Model, Serializable):
    __tablename__ = "locations"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="locations")
    contact_phone = Column(String)
    name = Column(String)
    contact_email = Column(String)
    contact_family_name = Column(String)
    contact_given_name = Column(String)
    host_given_name = Column(String)
    timezone = Column(String)
    city = Column(String)
    locality = Column(String)
    state = Column(String)
    address_type = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    accuracy = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    postal_code = Column(String)
    country = Column(String)
    modified_date = Column(DateTime)
    created_date = Column(DateTime)
    number_spaces_remaining = Column(Integer)
    spaces_remaining = Column(Boolean)
    primary = Column(Boolean)

    def __init__(self, **attrs):
        encoded = ascii_keys(attrs)
        super(Location, self).__init__(**encoded)

    def __repr__(self):
        return "<Location id: %s, name: %s, event_id: %s>" % (self.id, self.name, self.event_id)

    def serialized_attrs(self):
        return ["id", "name", "contact_email", "contact_phone", "contact_family_name",
         "contact_given_name", "host_given_name", "city", "state",
         "address1", "address2", "number_spaces_remaining",
         "spaces_remaining"]
