from flask import Flask, request
from flask.json import jsonify
from app.database import DB
from app.models import Event, Location, Attendee
from app.json_encoder import DecimalSafeJSONEncoder
from flask_cors import CORS

app = Flask(__name__)
app.json_encoder = DecimalSafeJSONEncoder
CORS(app)

def db():
    return app.config["db"]

def query(model):
    return db().session.query(model)

def all_locations():
    return query(Location).all()

def page_number(request):
    try:
        return max([1, int(request.args["page"])])
    except Exception:
        return 1

@app.route("/events", methods=["GET"])
def show_events():
    return jsonify(map(lambda event: event.serialize(),
                       Event.paged(db(), page_number(request))))

@app.route("/events", methods=["POST"])
def create_event():
    event = Event(**request.json)
    db().save_records(event)
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
    db().save_records(loc)
    return jsonify({"success": True,
                    "location": loc.serialize()})

@app.route("/locations/<int:location_id>")
def show_location(location_id):
    loc = query(Location).filter(Location.id == location_id).first()
    return jsonify(loc.serialize())

@app.route("/events/<int:event_id>/attendees", methods=["POST"])
def create_attendee(event_id):
    event = query(Event).filter(Event.id == event_id).first()
    user_info = request.json
    attendee = Attendee(**user_info)
    event.attendees.append(attendee)

    try:
        db().save_records(event, attendee)
        return jsonify(map(lambda a: a.serialize(), event.attendees))
    except Exception:
        return jsonify(map(lambda a: a.serialize(), event.attendees))

@app.route("/events/<int:event_id>/attendees", methods=["DELETE"])
def delete_attendee(event_id):
    event = query(Event).filter(Event.id == event_id).first()
    user_info = request.json
    attendee = query(Attendee).filter(Attendee.event_id == event_id,
                                      Attendee.name == user_info["name"],
                                      Attendee.email == user_info["email"])
    if attendee:
        attendee.delete()

    return jsonify(map(lambda a: a.serialize(), event.attendees))
