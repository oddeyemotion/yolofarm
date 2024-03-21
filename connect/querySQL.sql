CREATE DATABASE yolofarm

USE yolofarm

IF EXISTS (SELECT * FROM SYS.objects WHERE NAME = 'Temperature')
	DROP TABLE Temperature
GO
CREATE TABLE Temperature
(
	Date_   Datetime NOT NULL,
	Temp	Int
)

ALTER TABLE Temperature
	ADD CONSTRAINT PK_Temp PRIMARY KEY (Date_)
