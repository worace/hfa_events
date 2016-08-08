# Events App

## Setup / Running

```sh
vagrant up
vagrant ssh
source env/bin/activate
cd backend
nosetests
cd ..
honcho start
```
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


#### Data
We have 2 tables, Events and Locations (each event has a single location)

Events look like:
Events:
```
    id (Integer)
    status (String)
    start_date (DateTime)
    end_date (DateTime)
    description (String)
    official (Boolean)
    visibility (String)
    guests_can_invite_others (Boolean)
    modified_date (DateTime)
    created_date (DateTime)
    participant_count (Numeric)
    reason_for_private (String)
    order_email_template (String)
    name (String)
    locations = (Location)
```

Locations:
```
	id (Integer)
    event_id (Integer, links to parent event's id)

    address_type (String)
    contact_phone (String)
    primary (Boolean)
    contact_email (String)
    contact_family_name (String)
    contact_given_name (String)
    host_given_name (String)
    timezone (String)
    city (String)
    locality (String)
    state (String)
    address_type (String)
    latitude (String)
    longitude (String)
    accuracy (String)
    address1 (String)
    address2 (String)
    postal_code (String)
    country (String)
    modified_date (DateTime)
    created_date (DateTime)
    number_spaces_remaining (Numeric)
    spaces_remaining (Boolean)
    name (String)
```
