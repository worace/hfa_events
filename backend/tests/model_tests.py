from app.models import Event, Location
from nose.tools import *
import datetime
from test_helper import AppTestCase

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


class ModelTests(AppTestCase):
    def test_creates_event_from_dict(self):
        event = Event(**event_data)
        assert_equal("confirmed", event.status)

    def test_creates_location_from_dict(self):
        location = Location(**location_data)
        assert_equal("Pizza", location.contact_family_name)
        assert_equal("Man", location.contact_given_name)

    def test_paginating_models(self):
        names = []
        for i in range(12):
            names.append("Event #%s" % i)

        for n in names:
            Event.create(self.db, **{"name": n})

        page1 = Event.paged(self.db, 1, 10)
        page2 = Event.paged(self.db, 2, 10)

        assert_equal(names[0:10], map(lambda e: e.name.encode("ascii"), page1))
        assert_equal(names[10:12], map(lambda e: e.name.encode("ascii"), page2))

