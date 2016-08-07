import React from 'react';
import UserStore from './user_store'

const UserInfo = React.createClass({
  getInitialState: function() {
    return { isLoggedIn: UserStore.isLoggedIn(),
             userInfo: UserStore.userInfo(),
             nameField: "",
             emailField: "" }
  },
  logIn: function(event) {
    event.preventDefault();
    UserStore.logIn(this.state.nameField, this.state.emailField);
    this.setState({isLoggedIn: UserStore.isLoggedIn(), userInfo: UserStore.userInfo()})
  },
  logOut: function(event) {
    event.preventDefault();
    UserStore.logOut();
    this.setState({isLoggedIn: UserStore.isLoggedIn(), userInfo: UserStore.userInfo()})
  },
  nameChanged: function(event) {
    this.setState({nameField: event.target.value});
  },
  emailChanged: function(event) {
    this.setState({emailField: event.target.value});
  },
  render: function() {
    if (this.state.isLoggedIn) {
      return (
        <div>
          <p>Welcome back, {this.state.userInfo.name} <small>({this.state.userInfo.email})</small></p>
          <a href="#" onClick={this.logOut}>Log Out</a>
        </div>
      );
    } else {
      return (
        <div>
          <p>Please Log In!</p>

          <form onSubmit={this.logIn}>
            <div className="form-group">
              <label htmlFor="inputEmail">Email address</label>
              <input type="email" className="form-control" id="inputEmail" onChange={this.emailChanged} value={this.state.emailField} placeholder="Enter email" />
            </div>
            <div className="form-group">
              <label htmlFor="inputName">Name</label>
              <input type="text" className="form-control" id="inputName" onChange={this.nameChanged} value={this.state.nameField} placeholder="Name" />
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
          </form>
        </div>
      )
    }
  }
});

module.exports = UserInfo;