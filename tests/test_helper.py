from flask_testing import TestCase
from flask import Flask
from app.server import app

class AppTestCase(TestCase):
    def setup(self):
        # TODO -- import app
        # TODO -- configure and init db
        pass

    def teardown(self):
        # TODO -- disconnect from db
        # TODO -- remove test data / wipe to orig schema?
        pass

    def create_app(self):
        return app
