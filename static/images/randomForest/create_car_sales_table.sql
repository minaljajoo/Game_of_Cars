USE cardb_test;

DROP TABLE IF EXISTS car_sales;

CREATE TABLE car_sales(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        model VARCHAR(255),
		month VARCHAR (50),
    Year_2015 INT,
    Year_2016 INT,
    Year_2017 INT,
    Year_2018 INT,
    Year_2019 INT
);

SELECT * FROM car_sales;