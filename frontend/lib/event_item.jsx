import React from 'react';
import moment from "moment";
import UserStore from './user_store'
import $ from "jquery"
import API from "./api"

// Attendance / RSVP
// - Have event return list of attendees as part of api payload
// - 1 check if logged in
// - 2 check if your user info appears in list of attendees

// If so: show Un-rsvp button
// If not: show RSVP button

const EventItem = React.createClass({
  componentDidMount: function() {
    $(UserStore).on("authStatusChanged", function(event) {
      this.setState({isLoggedIn: UserStore.isLoggedIn(),
                     userInfo: UserStore.userInfo()});
    }.bind(this));
  },
  getInitialState: function() {
    return {isExpanded: false,
            isLoggedIn: UserStore.isLoggedIn(),
            userInfo: UserStore.userInfo(),
            event: this.props.event};
  },
  formattedDate: function() {
    let start = this.state.event.start_date;
    return moment(start).format("ddd, MMMM Do YYYY");
  },
  formattedTime: function(dateString) {
    return moment(dateString).format("h:mm a");
  },
  formattedStartTime: function() {
    return this.formattedTime(this.state.event.start_date);
  },
  formattedEndTime: function() {
    return this.formattedTime(this.state.event.end_date);
  },
  cityState: function() {
    let loc = this.state.event.location_info
    return loc.city + ", " + loc.state;
  },
  signedUpCount: function() {
    let count = this.state.event.attendee_info.length;
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
  details: function() {
    if (this.state.isExpanded) {
      return (

        <div className="row col-sm-12">
          <div className="col-sm-9">
            <p>{this.state.event.description}</p>
          </div>
          <div className="col-sm-3">
            <p>{this.attendeeList()}</p>
          </div>
        </div>
      )
    } else {
      return null;
    }
  },
  moreOrLess: function() {
    let text = {true: "Less", false: "More"}[this.state.isExpanded];
    let toggle = function(event) {
      event.preventDefault();
      this.setState({isExpanded: !this.state.isExpanded});
    }.bind(this);

    return <p className="col-sm-12"><a href="#" onClick={toggle}>{text}</a></p>
  },
  isAttendee: function(userInfo) {
    let attendees = this.state.event.attendee_info;
    for (let i = 0; i < attendees.length; i++) {
      let att = attendees[i];
      if (att.name === userInfo.name && att.email === userInfo.email) {
        return true;
      }
    }
    return false;
  },
  isAttending: function() {
    return (this.state.isLoggedIn && this.isAttendee(this.state.userInfo));
  },
  updateAttendees: function(newAttendees) {
    let event = this.state.event;
    event.attendee_info = newAttendees;
    this.setState({event: event});
  },
  updateRSVP: function(isGoing) {
    if (!this.state.isLoggedIn) {
      window.alert("login!");
      return;
    }

    let handler = isGoing ? API.eventRSVP : API.eventUnRSVP;

    handler(this.state.event.id,
            this.state.userInfo).then(this.updateAttendees);
  },
  attendeeList: function() {
    let attendees = this.state.event.attendee_info;
    if (attendees.length > 0) {
      let items = this.state.event.attendee_info.map(function(att, idx) {
        return (<li key={idx}>{att.name}</li>);
      });
      return (<div><p>Who's going:</p><ul>{items}</ul></div>)
    } else {
      return null;
    }
  },
  rsvpButton: function() {
    if (this.isAttending()) {
      // janky currying
      let handler = function() { this.updateRSVP(false) }.bind(this);
      return <button className="btn btn-danger" type="submit" onClick={handler}>Not Going</button>
    } else {
      let handler = function() { this.updateRSVP(true) }.bind(this);
      return <button className="btn btn-success" type="submit" onClick={handler}>I'm Going!</button>
    }
  },
  render: function() {
    return(
      <div className="row event">
        <div className="row col-sm-12">
          <div className="col-sm-3">
            <p>{this.formattedDate()}</p>
            <p><strong>{this.formattedStartTime()} to {this.formattedEndTime()}</strong></p>
          </div>

          <div className="col-sm-6">
            <h4>{this.state.event.name}</h4>
            <p>{this.state.event.location_info.address1}</p>
            <p>{this.cityState()}</p>
          </div>

          <div className="col-sm-3">
            <p>{this.signedUpCount()}</p>
            <p>Are You Going?</p>
            {this.rsvpButton()}
          </div>
        </div>

        <div className="row col-sm-12">
          {this.moreOrLess()}
        </div>

        {this.details()}

      </div>
    )
  }
});

module.exports = EventItem;
