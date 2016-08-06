from flask import Flask
from flask.json import jsonify
import app.database as db

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({"db": db.session})

@app.route("/events")
def show_events():
    return jsonify([])
