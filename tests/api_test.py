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

    def test_fetching_locations(self):
        response = self.client.get("/locations")
        assert_equal(response.status_code, 200)
        assert_equal([], response.json)

    def test_creating_a_location(self):
        location_json = self.read_file("./tests/sample_location.json")
        location_data = json.loads(location_json)
        for k in ["id", "modified_date", "created_date"]:
            location_data.pop(k, None)

        # Create an event for our location to point to
        event_json = self.read_file("./tests/sample_event.json")
        event_data = json.loads(event_json)
        for k in ["id", "modified_date", "created_date"]: event_data.pop(k, None)
        response = self.post_json("/events", event_data)

        location_data["event_id"] = response.json["event"]["id"]

        response = self.post_json("/locations", location_data)
        assert_equal(response.status_code, 200)

        location_id = response.json["location"]["id"]
        response = self.client.get("/locations/%s" % location_id)
        assert_equal(response.status_code, 200)
        assert_equal(location_data["name"], response.json["name"])

        response = self.client.get("/locations")
        assert_equal(1, len(response.json))
