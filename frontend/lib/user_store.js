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
  logIn: function(name, email) {
    let storage = window.localStorage;
    storage.setItem("userName", name);
    storage.setItem("userEmail", email);
  },
  logOut: function() {
    let storage = window.localStorage;
    storage.removeItem("userName");
    storage.removeItem("userEmail");
  },
  isLoggedIn: function() {
    console.log("Checking logged in", this.userInfo());
    return (this.userInfo() !== null);
  }
}

module.exports = UserStore;
