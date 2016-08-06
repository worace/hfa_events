from nose.tools import *
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql:///hfa_events')
# engine.echo = True
metadata = MetaData(bind=engine)

def test_making_sql_conn():
    events = Table("events", metadata, autoload=True)
    assert_equal("UWS Voter Registration", events.select().execute().first()["name"])

    locs = Table("locations", metadata, autoload=True)
    assert_equal("72 nd Street Train Station", locs.select().execute().first()["name"])

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    locations = relationship("Location", back_populates="event")

    def __repr__(self):
        return "<Event id: %s, name: %s>" % (self.id, self.name)

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="locations")

    def __repr__(self):
        return "<Location id: %s, name: %s, event_id: %s>" % (self.id, self.name, self.event_id)

Session = sessionmaker(bind=engine)
session = Session()


def test_using_orm():
    Base.metadata.create_all(engine)
    an_event = Event(name = "Pizza Party")
    assert_equal("Pizza Party", an_event.name)
    session.add(an_event)
    session.commit()
    assert_equal(int, type(an_event.id) )
    our_event = session.query(Event).order_by(Event.id.desc()).first()
    assert_equal("Pizza Party", our_event.name)

def test_using_relationships():
    event = session.query(Event).first()
    loc = event.locations[0]
    assert_equal(Location, type(loc))
    assert_equal(event.id, loc.event_id)
