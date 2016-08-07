import $ from "jquery";

let API = {
  getEvents: function(pageNumber) {
    return $.get("http://localhost:5000/events?page=" + (pageNumber || 1));
  },
  eventRSVP: function(eventID, userInfo) {
    let url = "http://localhost:5000/events/" + eventID + "/attendees"
    return $.ajax({url: url,
                   method: "POST",
                   data: JSON.stringify(userInfo),
                   contentType: "application/json" });
  },
  eventUnRSVP: function(eventID, userInfo) {
    let url = "http://localhost:5000/events/" + eventID + "/attendees"
    return $.ajax({url: url,
                   method: "DELETE",
                   data: JSON.stringify(userInfo),
                   contentType: "application/json" });
  },
}

module.exports = API;
