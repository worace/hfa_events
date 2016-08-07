import $ from "jquery";

let API = {
  getEvents: function(baseUrl) {
    return $.get("http://localhost:5000/events");
  },
  eventRSVP: function(eventID, userInfo) {
    let url = "http://localhost:5000/events/" + eventID + "/attendees"
    return $.post(url, userInfo);
  }
}

module.exports = API;
