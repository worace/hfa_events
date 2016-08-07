import React from 'react';
import moment from "moment";

const EventItem = React.createClass({
  getInitialState: function() {
    return {isExpanded: false};
  },
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
  details: function() {
    if (this.state.isExpanded) {
      return <p>{this.props.event.description}</p>
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
  render: function() {
    return(
      <div className="row event">
        <div className="row col-sm-12">
          <h3 className="col-sm-12">{this.props.event.name}</h3>
        </div>

        <div className="row col-sm-12">
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