from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Model
from sqlalchemy import desc
from app.models.shared import Serializable, Pageable, ascii_keys

class Location(Model, Serializable, Pageable):
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
