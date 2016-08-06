from flask_testing import TestCase
from flask import Flask
from app.server import app
from app.models import Event, Location
import json

class AppTestCase(TestCase):
    def setUp(self):
        app.config["db"].session.query(Location).delete()
        app.config["db"].session.query(Event).delete()

    def tearDown(self):
        app.config["db"].session.query(Location).delete()
        app.config["db"].session.query(Event).delete()

    def create_app(self):
        return app

    def read_file(self, path):
        f = open(path)
        contents = f.read()
        f.close()
        return contents

    def post_json(self, path, value):
        payload = json.dumps(value)
        return self.client.post(path,
                                data = payload,
                                content_type = "application/json")
