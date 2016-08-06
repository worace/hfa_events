from app.models import Event
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

@nottest
def test_creates_event_from_dict():
    event = Event(**event_data)
    assert_equal("confirmed", event.status)
    start = datetime.datetime(2015, 8, 22, 17,0,0)
    assert_equal(start, event.start_date)

