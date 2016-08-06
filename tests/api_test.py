from nose.tools import *
from test_helper import AppTestCase

class ApiTest(AppTestCase):
    def test_fetching_events(self):
        response = self.client.get("/events")
        assert_equal(response.status_code, 200)
        assert_equal([], response.json)

