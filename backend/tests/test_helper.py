from flask_testing import TestCase
from flask import Flask
from app.models.event import Event
from app.models.location import Location
from app.models.attendee import Attendee
from app.server import app
from app.database import DB
import json

class AppTestCase(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        db = DB("hfa_events_test")
        db.init_db()
        self.db = db
        app.config.update({"db": db})

        app.config["db"].session.query(Location).delete()
        app.config["db"].session.query(Attendee).delete()
        app.config["db"].session.query(Event).delete()

    def tearDown(self):
        app.config["db"].session.close()
        app.config["db"].connection.close()

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

    def delete_json(self, path, value):
        payload = json.dumps(value)
        return self.client.delete(path,
                                  data = payload,
                                  content_type = "application/json")
