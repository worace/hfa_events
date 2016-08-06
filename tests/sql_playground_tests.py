from nose.tools import *
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import DB
from app.models import Event, Location

db = DB("hfa_events_dev")
db.init_db()

@nottest
def test_making_sql_conn():
    metadata = MetaData(db.engine)
    events = Table("events", metadata, autoload=True)
    assert_equal("UWS Voter Registration", events.select().execute().first()["name"])

    locs = Table("locations", metadata, autoload=True)
    assert_equal("72 nd Street Train Station", locs.select().execute().first()["name"])

def test_using_orm():
    an_event = Event(name = "Pizza Party")
    assert_equal("Pizza Party", an_event.name)
    db.session.add(an_event)
    db.session.commit()
    assert_equal(int, type(an_event.id) )
    our_event = db.session.query(Event).order_by(Event.id.desc()).first()
    assert_equal("Pizza Party", our_event.name)

def test_using_relationships():
    event = db.session.query(Event).first()
    loc = event.locations[0]
    assert_equal(Location, type(loc))
    assert_equal(event.id, loc.event_id)
