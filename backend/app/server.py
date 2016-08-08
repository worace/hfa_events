from flask import Flask, request
from flask.json import jsonify
from app.database import DB
from app.models.event import Event
from app.models.location import Location
from app.models.attendee import Attendee
from app.json_encoder import DecimalSafeJSONEncoder
from flask_cors import CORS

app = Flask(__name__)
app.json_encoder = DecimalSafeJSONEncoder
CORS(app)

def db():
    return app.config["db"]

def page_number(request):
    try:
        return max([1, int(request.args["page"])])
    except Exception:
        return 1

@app.route("/events", methods=["GET"])
def show_events():
    events = Event.paged_with_associations(db(), page_number(request), 10)
    return jsonify(map(lambda event: event.serialize(), events))

@app.route("/events", methods=["POST"])
def create_event():
    event = Event.create(db(), **request.json)
    return jsonify({"success": True,
                    "event": event.serialize()})

@app.route("/events/<int:event_id>")
def show_event(event_id):
    event = Event.find_with_associations(db(), event_id)
    return jsonify(event.serialize())

@app.route("/locations", methods=["GET"])
def show_locations():
    return jsonify(map(lambda location: location.serialize(),
                       Location.paged(db(), page_number(request))))

@app.route("/locations", methods=["POST"])
def create_location():
    loc = Location.create(db(), **request.json)
    return jsonify({"success": True,
                    "location": loc.serialize()})

@app.route("/locations/<int:location_id>")
def show_location(location_id):
    loc = Location.find(db(), location_id)
    return jsonify(loc.serialize())

@app.route("/events/<int:event_id>/attendees", methods=["POST"])
def create_attendee(event_id):
    event = Event.find(db(), event_id)
    attendee = Attendee(**request.json)
    event.attendees.append(attendee)

    try:
        db().save_records(event, attendee)
        return jsonify(map(lambda a: a.serialize(), event.attendees))
    except Exception:
        return jsonify(map(lambda a: a.serialize(), event.attendees))

@app.route("/events/<int:event_id>/attendees", methods=["DELETE"])
def delete_attendee(event_id):
    event = Event.find(db(), event_id)
    user_info = request.json
    attendee = db().query(Attendee).filter(Attendee.event_id == event_id,
                                           Attendee.name == user_info["name"],
                                           Attendee.email == user_info["email"])
    if attendee:
        attendee.delete()

    return jsonify(map(lambda a: a.serialize(), event.attendees))
