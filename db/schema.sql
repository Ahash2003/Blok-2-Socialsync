DROP SCHEMA IF EXISTS `YOUR_DATABASE_SCHEMA`;    
CREATE SCHEMA `YOUR_DATABASE_SCHEMA`;
USE `DATABASE_BLOK_2`;

-- https://www.w3schools.com/sql/sql_comments.asp
-- Create a User table, we probably need a login system

CREATE TABLE `user`(
    -- Minimal user table, adjust up to your needs
	`userId` INT NOT NULL AUTO_INCREMENT,	
    `firstname` VARCHAR(50),
    `lastname` VARCHAR(100),
	`emailadress` VARCHAR(255),
    `password` VARCHAR(32) NOT NULL,
    `telephonenumber` VARCHAR(15),
    PRIMARY KEY(`userId`)
);

--Add your create tables SQL here. Make sure to include the indexes!
-- Alternative: use an ORM like SQLAlchemy. Then you will not need this file.