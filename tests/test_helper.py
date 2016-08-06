from flask_testing import TestCase
from flask import Flask
from app.server import app
from app.models import Event, Location

class AppTestCase(TestCase):
    def setUp(self):
        # TODO -- import app
        # TODO -- configure and init db

        app.config["db"].session.query(Event).delete()
        app.config["db"].session.query(Location).delete()

        pass

    def tearDown(self):
        # TODO -- disconnect from db
        # TODO -- remove test data / wipe to orig schema?

        app.config["db"].session.query(Event).delete()
        app.config["db"].session.query(Location).delete()

        pass

    def create_app(self):
        return app
