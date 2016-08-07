require("./node_modules/bootstrap/dist/css/bootstrap.min.css")
require("./styles.css")
import React from 'react';
import ReactDOM from 'react-dom';
import API from "./lib/api";
import moment from "moment";

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

      console.log("received events:", events)
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
      <div>
      <div className="events">
        { this.eventElements() }
      </div>
      </div>
    );
  }
});

const EventItem = React.createClass({
  formattedDate: function() {
    let start = this.props.event.start_date;
    return moment(start).format("ddd, MMMM Do YYYY");
  },
  formattedTime: function(dateString) {
    return moment(dateString).format("h:mm a");
  },
  formattedStartTime: function() {
    return this.formattedTime(this.props.event.start_date);
  },
  formattedEndTime: function() {
    return this.formattedTime(this.props.event.end_date);
  },
  cityState: function() {
    let loc = this.props.event.location_info
    return loc.city + ", " + loc.state;
  },
  signedUpCount: function() {
    let count = this.props.event.participant_count;
    switch (count) {
      case 0:
        return "0 people going";
        break;
      case 1:
        return "1 person going"
        break;
      default:
        return count + " people going";
    }
  },
  render: function() {
    return(
      <div className="row event">
        <h3>{this.props.event.name}</h3>
        <div className="col-sm-2">
          <p>{this.formattedDate()}</p>
          <p>{this.formattedStartTime()} to {this.formattedEndTime()}</p>
        </div>

        <div className="col-sm-6">
          <p>{this.props.event.location_info.address1}</p>
          <p>{this.cityState()}</p>
        </div>

        <div className="col-sm-3">
          <p>{this.signedUpCount()}</p>
          <p>Are You Going?</p>
          <button className="btn btn-default" type="submit">No</button>
          <button className="btn btn-default" type="submit">Yes</button>
        </div>

      </div>
    )
  }
});

ReactDOM.render(<EventsList/>, document.querySelector("#myApp"));
