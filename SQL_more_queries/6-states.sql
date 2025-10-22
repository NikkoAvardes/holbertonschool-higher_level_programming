-- Crée la base de données hbtn_0d_usa et la table states avec id (PRIMARY KEY AUTO_INCREMENT) et name (VARCHAR(256) NOT NULL)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
