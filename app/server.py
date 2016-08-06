from flask import Flask, request
from flask.json import jsonify
from app.database import DB
from app.models import Event, Location

db = DB("hfa_events_test")
db.init_db()

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({"db": db})

def query(model):
    return db.session.query(model)

def all_events():
    return query(Event).all()

def all_locations():
    return query(Location).all()

@app.route("/events", methods=["GET"])
def show_events():
    #TODO -- probably want to paginate these
    return jsonify(map(lambda event: event.serialize(),
                       all_events()))

@app.route("/events", methods=["POST"])
def create_event():
    event = Event(**request.json)
    db.session.add(event)
    db.session.commit()
    return jsonify({"success": True,
                    "event": event.serialize()})

@app.route("/events/<int:event_id>")
def show_event(event_id):
    event = query(Event).filter(Event.id == event_id).first()
    return jsonify(event.serialize())

@app.route("/locations", methods=["GET"])
def show_locations():
    #TODO -- probably want to paginate these
    return jsonify(map(lambda location: location.serialize(),
                       all_locations()))

@app.route("/locations", methods=["POST"])
def create_location():
    loc = Location(**request.json)
    db.session.add(loc)
    db.session.commit()
    return jsonify({"success": True,
                    "location": loc.serialize()})

@app.route("/locations/<int:location_id>")
def show_location(location_id):
    loc = query(Location).filter(Location.id == location_id).first()
    return jsonify(loc.serialize())
