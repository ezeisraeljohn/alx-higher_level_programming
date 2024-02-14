-- create the database hbtn_0d_usa if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- create a table cities
CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id),
    name VARCHAR(256) NOT NULL
    );
