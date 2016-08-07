-- Events
CREATE TABLE IF NOT EXISTS events (
  id serial PRIMARY KEY,
  status varchar(255),
  start_date timestamp,
  end_date timestamp,
  description varchar(1024),
  official boolean,
  visibility varchar(255),
  guests_can_invite_others boolean,
  modified_date timestamp,
  created_date timestamp,
  participant_count integer,
  reason_for_private varchar(255),
  order_email_template varchar(255),
  name varchar(255)
);

-- Locations
CREATE TABLE IF NOT EXISTS locations (
  id serial PRIMARY KEY,
  event_id integer REFERENCES events (id),
  "primary" boolean,
  contact_phone varchar(255),
  name varchar(255),
  contact_email varchar(255),
  contact_family_name varchar(255),
  contact_given_name varchar(255),
  host_given_name varchar(255),
  timezone varchar(255),
  city varchar(255),
  locality varchar(255),
  state varchar(255),
  address_type varchar(255),
  latitude varchar(255),
  longitude varchar(255),
  accuracy varchar(255),
  address1 varchar(255),
  address2 varchar(255),
  postal_code varchar(255),
  country varchar(255),
  modified_date timestamp,
  created_date timestamp,
  number_spaces_remaining integer,
  spaces_remaining boolean
);

CREATE INDEX location_event_id ON locations (event_id);

CREATE TABLE IF NOT EXISTS attendees (
  id serial PRIMARY KEY,
  event_id integer REFERENCES events (id),
  name varchar(255),
  email varchar(255),
  modified_date timestamp,
  created_date timestamp
);

CREATE INDEX attendee_event_id ON attendees (event_id);
CREATE UNIQUE INDEX attendees_name_email_event ON attendees (event_id, email, name);
