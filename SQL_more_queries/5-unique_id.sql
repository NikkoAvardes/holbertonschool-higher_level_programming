-- Crée la table unique_id avec id (INT DEFAULT 1 UNIQUE) et name (VARCHAR(256))
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
