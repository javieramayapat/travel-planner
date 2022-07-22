CREATE DATABASE travel_planner;

-- switch connection to a new database
\c travel_planner;

CREATE TABLE users(
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    username varchar(100) NOT NULL UNIQUE,
    email varchar(150) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE trips (
    id bigserial NOT NULL,
    user_id bigint NOT NULL,
    origin_name VARCHAR(100) NOT NULL,
    destination_name VARCHAR(10) NOT NULL,
    departure_date timestamp  NOT NULL,
    arrival_date timestamp  NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);


INSERT INTO users (id, name, last_name, username, email, password) VALUES (1, 'Javier', 'Amaya','javieramayapat', 'javier@gmail.com', 'easypassword');


-- INSERT INTO trips(id, user_id, origin_name, destination_name, departure_date, arrival_date) VALUES (1, 1,'Mexico','Spain','2021-07-21 05:25:01','2021-07-21 08:25:01');
-- INSERT INTO trips(id, user_id, origin_name, destination_name, departure_date, arrival_date) VALUES (2, 1,'Spain','France','2021-07-22 10:25:01','2021-07-21 08:25:01');