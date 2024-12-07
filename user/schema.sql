DROP TABLE IF EXISTS User;

CREATE TABLE User(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birthday TEXT,
    height INTEGER,
    weight INTEGER,
    gender TEXT,
    username TEXT UNIQUE NOT NULL,
    FOREIGN KEY(username) REFERENCES Account(username)
);