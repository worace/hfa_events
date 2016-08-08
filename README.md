# Events App

## Setup / Running

Extracting the tarball:

```
tar -xzf horace_hfa_events_app.tar.gz
cd hfa_events
```

The project is split into 2 subdirectories:

```
hfa_events
|__backend/(python stuff)
|__frontend/(JS stuff)
```

To run it, use these steps:

```sh
vagrant up
vagrant ssh
source env/bin/activate
cd backend
nosetests
cd ..
honcho start
```

Vagrant should forward the ports so that:

* Frontend app (a webpack server) is visible on port 3000
* Backend app (a flask server) is visible running on 9292

Open the frontend app in your browser: [http://localhost:3000](http://localhost:3000).

**Setup Note:** I modified the Vagrantfile to add some automated setup for my own dependencies. It includes a script that looks for the PG file as `data.pgdump` in the project root directory, so if you're going to replace this file make sure you put it in the same place and do it before running `vagrant up`.

I also had a long fight with vagrant trying to get it to install my node modules properly but never got it working. So for now I've had to install npm modules on the host machine and include them in the zip file.

## Notes

### Process / Decisions

**Backend**

* I started out with the backend app since the tools here were new to me and I wanted to get a feel for them
* I was able to get a good testing setup going with nose and then use this both to drive the app code but also as a framework for experimenting with flask and sqlalchemy along the way
* The main backend endpoints are `/event`, `/locations`, `/events/<:id>`, `/locations/<:id>`, and `POST /events/<id>/attendees` (for RSVPing to an event).
* Endpoints return JSON and the index endpoints are paged with a `?page=<num>` query param
* I included a few other endpoints that I needed for testing (so I could test from an empty db and create records via the API as needed)
* "Events" are the most important resource in the API, and in desigining it I decided to flatten some of the relationships (event's location and attendee list) into the main event index response. This simplifies querying on the frontend since we don't have to make a second request to get details of a single event. The downside is it obviously bloats the size of the payload, but I felt like I had controlled this via pagination (so no single batch can get too large) and was ok with the tradeoff.

**Frontend**

* The frontend is a React app consisting of a handful of components and built using webpack; it uses simple Jquery ajax requests to communicate with the API
* The main queries it makes are fetching batches of events and sending POST or DELETE requests to RSVP to an event
* **Login** -- For the sake of time I just put together a simplistic "login" system using localstorage -- first time viewers of the site will see a basic name/email form where they can login.
* The RSVP system simply takes on name/email so there's no strong protection against users using the same email or name. These would obviously be some of the main benefits of adding in a stronger server-side login process. That said, a user's RSVP's should "persist" from the perspective of the frontend if they log out and log in again
* The frontend has a really basic "infinite scroll" button at the bottom to fetch more events; this still needs a bit more intelligence behind it to be able to update the UI when there are no more pages, but it works as a proof of concept.

## What's Missing

* **Better DB Migrations** All of this tooling was new to me so I didn't have time to figure out a better solution for this. Currently my "migrations" are just a sql file that gets run to set up the current schema.
* **Authentication** As mentioned above I just mocked this out using localstorage. I tried to put it behind a reasonable interface (`UserStore`) in the frontend so it could potentially be transitioned more easily.
* Better error handling and validation on API parameters -- currently most of the "creation" endpoints are just used in my tests, so they don't have a ton of validation on them
* Pagination metadata in API responses -- The pagination currently just spits back batches of events. Ultimately I'd want to include some metadata about this in the response, so the payload might look like `{pagination: {current: 1, this_batch: 10, total: 1258}, events: [...]}`
* **Build / Deployment pipeline** -- Just using webpack as a means of building and serving the frontend. Would eventually need to sort out building this into a static asset bundle and deployin that somehow. Ditto for the backend app.

### Assignment

#### What to do
- Install Virtualbox and vagrant
- `vagrant up`
- `vagrant ssh`
- In your home folder find data.pgdump
- Import the file data.pgdump into postgres (its already installed on the vagrant machine)
- Write a backend service for the specified api using python
- Write a frontend service that consumes that api and provides an interface for the user

#### Task
Today we're building a simple events website. We've been provided data for a bunch of events which include location data. We'd like to build an interface to allow users to view and edit the data. We need both a backend that has endpoints that take in parameters and returns json data, and a frontend interface which consumes the data and displays it.


#### Backend Endpoints
We need endpoints to:
- List out all events (there could be thousands)
- Give details on a specific event
- Attend/RSVP to an event

You can choose what the endpoint(s) look like and what data they return but make sure that we can accomplish all the above tasks. Just make sure the endpoints return json.

#### Frontend
- Render the list of events in chronological order, displaying whatever details you deem necessary for each event
- Allow a user to view more details about each event, including ticket tiers, event description, etc. You can display the details on the same page, or create a second "event details" page.
- Allow a user to mark an event as "attending" — if a user has marked an event as "attending," this state should be reflected in the list of events, as well as on the event details page.


#### General notes
* Include any assumptions you are making about the requirements for the project in your code comments.
* Make sure the project works in the latest versions of Chrome, Firefox, Safari and Internet Explorer. No need to support anything older than that.
* If you use a JS module loader or CSS precompiler, please do make sure to include the unminified version of your source when you submit the test.
* Don't worry too much about how it looks... But don't worry too little!

#### To Submit
Once you have your code working, zip up the directory and submit it along with the command to start the server and the html page to goto.  When evaluating the interface we will be using a different dataset which is much larger.

