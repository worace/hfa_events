from nose.tools import *
from test_helper import AppTestCase
import json

class ApiTest(AppTestCase):
    def create_sample_event(self):
        event_json = self.read_file("./tests/sample_event.json")
        event_data = json.loads(event_json)
        for k in ["id", "modified_date", "created_date"]:
            event_data.pop(k, None)

        response = self.post_json("/events", event_data)
        event_data["id"] = response.json["event"]["id"]
        return (event_data, response)

    def create_sample_location(self, event_id):
        location_json = self.read_file("./tests/sample_location.json")
        location_data = json.loads(location_json)
        location_data["event_id"] = event_id

        for k in ["id", "modified_date", "created_date"]:
            location_data.pop(k, None)

        response = self.post_json("/locations", location_data)
        location_data["id"] = response.json["location"]["id"]
        return(location_data, response)

    def test_fetching_events(self):
        response = self.client.get("/events")
        assert_equal(response.status_code, 200)
        assert_equal([], response.json)

    def test_creating_an_event(self):
        event_data, response = self.create_sample_event()
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

        # Create an event for our location to point to
        event_data, event_response = self.create_sample_event()

        location_data, response = self.create_sample_location(event_response.json["event"]["id"])

        assert_equal(response.status_code, 200)
        location_id = response.json["location"]["id"]
        response = self.client.get("/locations/%s" % location_id)
        assert_equal(response.status_code, 200)
        assert_equal(location_data["name"], response.json["name"])
        response = self.client.get("/locations")
        assert_equal(1, len(response.json))

    def test_reading_event_attributes(self):
        self.create_sample_event()

        expected_attrs = [u"name", u"start_date", u"end_date",
                          u"description", u"participant_count",
                          u"status", u"id", u"location_info", u"attendee_info"]

        event = self.client.get("/events").json[0]
        assert_equal(sorted(expected_attrs), sorted(event.keys()))

    def test_reading_location_attributes(self):
        _, response = self.create_sample_event()
        self.create_sample_location(response.json["event"]["id"])

        expected_attrs = [u"id", u"name", u"contact_email", u"contact_phone",
                          u"contact_family_name", u"contact_given_name",
                          u"host_given_name", u"city", u"state",
                          u"address1", u"address2", u"number_spaces_remaining",
                          u"spaces_remaining"]

        event = self.client.get("/locations").json[0]
        assert_equal(sorted(expected_attrs), sorted(event.keys()))

    def test_event_includes_location_data_if_available(self):
        # Create an event for our location to point to
        event_data, event_response = self.create_sample_event()

        location_data, response = self.create_sample_location(event_response.json["event"]["id"])
        response = self.client.get("/events")
        event = response.json[0]

        assert_equal(location_data["name"], event["location_info"]["name"])

    def test_can_rsvp_for_an_event(self):
        event_data, event_response = self.create_sample_event()
        event_id = event_data["id"]

        user_info = {"name": "Horace", "email": "h@example.com"}

        path = "/events/%s/attendees" % event_id
        response = self.post_json(path, user_info)

        assert_equal(response.status_code, 200)
        assert_equal([user_info], response.json)

        updated_event = self.client.get("/events/%s" % event_id).json

        assert_equal([user_info], updated_event["attendee_info"])

