-- This creates a database and a user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

USE hbtn_0d_2;

-- Creates a user with the password user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT PRIVILEGE to the user created
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
