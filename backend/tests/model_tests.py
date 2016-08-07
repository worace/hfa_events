from app.models import Event, Location
from nose.tools import *
# from datetime import datetime
import datetime

event_data = {
    "status": "confirmed",
    "start_date": "2015-08-22 17:00:00",
    "end_date": "2015-08-22 19:00:00",
    "description": "desc",
    "official": False,
    "visibility": "public",
    "guests_can_invite_others": False,
    "participant_count": 8,
    "name": "UWS Voter Registration"
}

location_data = {
    "event_id": 1,
    "contact_phone": "1234567890",
    "contact_email": "example@example.com",
    "contact_family_name": "Pizza",
    "contact_given_name": "Man",
    "city": "New York",
    "latitude": 40.7787927,
    "longitude": -73.9820623,
    "address1": "72 nd Street at Broadway",
    "postal_code": "10024",
    "country": "US",
    "number_spaces_remaining": 42,
    "spaces_remaining": True,
    "name": "72 nd Street Train Station"
}

def test_creates_event_from_dict():
    event = Event(**event_data)
    assert_equal("confirmed", event.status)

def test_creates_location_from_dict():
    location = Location(**location_data)
    assert_equal("Pizza", location.contact_family_name)
    assert_equal("Man", location.contact_given_name)
