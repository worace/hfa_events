require("./node_modules/bootstrap/dist/css/bootstrap.min.css")
import React from 'react';
import ReactDOM from 'react-dom';
import API from "./lib/api";

const EventsList = React.createClass({
  getInitialState: function() {
    console.log("will get events..")
    API.getEvents().then(function(events) {
      this.setState({events: events});
    }.bind(this));
    return {events: []};
  },
  eventElements: function() {
    return this.state.events.map(function(event, index) {
      return(<EventItem event={event}/>);
    });
  },
  render: function() {
    return (
      <div>
      <ul className="events">
        { this.eventElements() }
      </ul>
      </div>
    );
  }
});

const EventItem = React.createClass({
  render: function() {
    return(
      <li>
        <p>{this.props.event.name}</p>
      </li>
    )
  }
});

ReactDOM.render(<EventsList/>, document.querySelector("#myApp"));
