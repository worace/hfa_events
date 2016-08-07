require("./node_modules/bootstrap/dist/css/bootstrap.min.css")
require("./styles.css")
import React from 'react';
import ReactDOM from 'react-dom';
import API from "./lib/api";
import UserInfo from "./lib/user_info"
import EventItem from "./lib/event_item"


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
    API.getEvents().then(function(events) {
      this.setState({events: events});
    }.bind(this));
    return {events: []};
  },
  eventElements: function() {
    return this.state.events.map(function(event, index) {
      return(<EventItem key={event.id} event={event}/>);
    });
  },
  render: function() {
    return (
      <div className="row">
        <div className="events col-sm-9">
          { this.eventElements() }
        </div>
        <div className="events col-sm-3">
          <UserInfo/>
        </div>
      </div>
    );
  }
});


ReactDOM.render(<EventsList/>, document.querySelector("#myApp"));
