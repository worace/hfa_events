import $ from "jquery";

let API = {
  getEvents: function(baseUrl) {
    return $.get("http://localhost:5000/events");
  }
}

module.exports = API;
