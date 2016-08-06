from nose.tools import *
from test_helper import AppTestCase
import json

class ApiTest(AppTestCase):
    def test_fetching_events(self):
        response = self.client.get("/events")
        assert_equal(response.status_code, 200)
        assert_equal([], response.json)

    def test_creating_an_event(self):
        event_json = self.read_file("./tests/sample_event.json")
        event_data = json.loads(event_json)
        for k in ["id", "modified_date", "created_date"]:
            event_data.pop(k, None)

        response = self.post_json("/events", event_data)
        assert_equal(response.status_code, 200)

        event_id = response.json["event"]["id"]
        response = self.client.get("/events/%s" % event_id)
        assert_equal(response.status_code, 200)
        assert_equal(event_data["name"], response.json["name"])

        response = self.client.get("/events")
        assert_equal(1, len(response.json))
