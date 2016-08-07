import $ from "jquery"

const UserStore = {
  userInfo: function() {
    let storage = window.localStorage;
    let name = storage.getItem("userName");
    let email = storage.getItem("userEmail");
    if (typeof name === "string" && typeof email === "string") {
      return {name: name, email: email};
    } else {
      return null;
    }
  },
  broadcastUpdate: function() {
    $(this).trigger("authStatusChanged");
  },
  logIn: function(name, email) {
    let storage = window.localStorage;
    storage.setItem("userName", name);
    storage.setItem("userEmail", email);
    this.broadcastUpdate();
  },
  logOut: function() {
    let storage = window.localStorage;
    storage.removeItem("userName");
    storage.removeItem("userEmail");
    this.broadcastUpdate();
  },
  isLoggedIn: function() {
    return (this.userInfo() !== null);
  }
}

module.exports = UserStore;
