DROP DATABASE IF EXISTS fuel_economy_db;

CREATE DATABASE fuel_economy_db;

USE fuel_economy_db;

DROP TABLE IF EXISTS Fuel;

CREATE TABLE Fuel(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
year INT,
model VARCHAR(50),
vehicle_class VARCHAR(50),
fuel_type VARCHAR(50),
smog_rating  INT,
city_mpg   INT,
hwy_mpg   INT,
cmb_mpg  INT,
Greenhouse_gas_score  INT,
smartway  VARCHAR(50)

);