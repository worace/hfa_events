from flask import Flask
from flask.json import jsonify
from app.database import DB
from app.models import Event

db = DB("hfa_events_test")
db.init_db()

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({"db": db})

def query(model):
    return db.session.query(model)

def all_events():
    return query(Event).all()

@app.route("/events", methods=["GET"])
def show_events():
    return jsonify(map(lambda event: event.serialize(),
                       all_events()))
