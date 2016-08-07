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
    let count = this.state.event.participant_count;
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
        <div>
          <p>{this.state.event.description}</p>

          {this.attendeeList()}
        </div>
      )
    } else {
      return null;
    }
  },
  moreOrLess: function() {
    let text = {true: "Less", false: "More"}[this.state.isExpanded];
    let toggle = function() {
      this.setState({isExpanded: !this.state.isExpanded});
    }.bind(this);

    return <button className="btn btn-default" type="submit" onClick={toggle}>{text}</button>
  },
  isAttendee: function(userInfo) {
    let result = false;
    let attendees = this.state.event.attendees;
    for (let i = 0; i < attendees.length; i++) {
      let att = attendees[i];
      if (att.name === userInfo.name && att.email === userInfo.email) {
        result = true;
        break;
      }
    }
    return result
  },
  isAttending: function() {
    return (this.state.isLoggedIn && this.isAttendee(this.state.userInfo));
  },
  rsvp: function() {
    if (!this.state.isLoggedIn) {
      window.alert("login!");
    } else {
      let p = API.eventRSVP(this.state.event.id, this.state.userInfo);
      p.then(function(updatedAttendees) {
        let event = this.state.event;
        event.attendee_info = updatedAttendees;
        this.setState({event: event})
      }.bind(this));
    }
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
  render: function() {
    return(
      <div className="row event">
        <div className="row col-sm-12">
          <h3 className="col-sm-12">{this.state.event.name}</h3>
        </div>

        <div className="row col-sm-12">
          <div className="col-sm-2">
            <p>{this.formattedDate()}</p>
            <p>{this.formattedStartTime()} to {this.formattedEndTime()}</p>
          </div>

          <div className="col-sm-6">
            <p>{this.state.event.location_info.address1}</p>
            <p>{this.cityState()}</p>
          </div>

          <div className="col-sm-3">
            <p>{this.signedUpCount()}</p>
            <p>Are You Going?</p>
            <button className="btn btn-default" type="submit" onClick={this.rsvp}>RSVP</button>
          </div>
        </div>


        <div className="row col-sm-12">
          <div className="col-sm-1">
            {this.moreOrLess()}
          </div>

          {this.details()}
        </div>

      </div>
    )
  }
});

module.exports = EventItem;
