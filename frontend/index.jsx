require("./node_modules/bootstrap/dist/css/bootstrap.min.css")
import React from 'react';
import ReactDOM from 'react-dom';
import API from "./lib/api";

/* - Render the list of events in chronological order,
     displaying whatever details you deem necessary for each event
 * - Allow a user to view more details about each event,
   including ticket tiers, event description, etc.
 * - You can display the details on the same page, or create a second "event details" page.
 * - Allow a user to mark an event as "attending"
   - if a user has marked an event as "attending," this state should be reflected in the list of events, as well as on the event details page.
 * */

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