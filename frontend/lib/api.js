import $ from "jquery";

const API_BASE_URL = process.env.API_BASE_URL || "http://localhost:5000"

function apiURL(path) {
  return API_BASE_URL + path;
}

let API = {
  getEvents: function(pageNumber) {
    return $.get(apiURL("/events?page=" + (pageNumber || 1)));
  },
  eventRSVP: function(eventID, userInfo) {
    let url = apiURL("/events" + eventID + "/attendees");
    return $.ajax({url: url,
                   method: "POST",
                   data: JSON.stringify(userInfo),
                   contentType: "application/json" });
  },
  eventUnRSVP: function(eventID, userInfo) {
    let url = apiURL("/events" + eventID + "/attendees");
    return $.ajax({url: url,
                   method: "DELETE",
                   data: JSON.stringify(userInfo),
                   contentType: "application/json" });
  },
}

module.exports = API;
