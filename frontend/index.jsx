require("./node_modules/bootstrap/dist/css/bootstrap.min.css")
require("./styles.css")
import React from 'react';
import ReactDOM from 'react-dom';
import API from "./lib/api";
import UserInfo from "./lib/user_info"
import EventItem from "./lib/event_item"

const EventsList = React.createClass({
  fetchNextPage: function() {
    this.fetchEvents(this.state.page + 1);
  },
  fetchEvents: function(page) {
    API.getEvents(page).then(function(events) {
      this.setState({events: this.state.events.concat(events), page: page});
    }.bind(this));
  },
  getInitialState: function() {
    this.fetchEvents(1);
    return {events: [], page: 1};
  },
  eventElements: function() {
    return this.state.events.map(function(event, index) {
      return(<EventItem key={event.id} event={event}/>);
    });
  },
  upcomingEvents: function() {
    let count = this.state.events.length;
    switch (count) {
      case 0:
        return "0 upcoming events";
        break;
      case 1:
        return "1 upcoming event";
        break;
      default:
        return count + " upcoming events";
    }
  },
  render: function() {
    return (
      <div>
        <div className="masthead-banner">
          <h1 className="masthead-header">Find an Event</h1>
          <p className="masthead-message">{this.upcomingEvents()}</p>
        </div>
        <div className="container">
          <div className="row">
            <div className="events col-sm-9">
              { this.eventElements() }
            </div>
            <div className="events col-sm-3">
              <UserInfo/>
            </div>
          </div>
          <div className="row">
            <button className="btn btn-primary" type="submit" onClick={this.fetchNextPage}>More Events</button>
          </div>
        </div>
      </div>
    );
  }
});


ReactDOM.render(<EventsList/>, document.querySelector("#myApp"));
