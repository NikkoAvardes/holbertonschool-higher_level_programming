-- Liste toutes les villes de Californie en utilisant une sous-requête (sans JOIN)
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
	SELECT id FROM states WHERE name = "California"
)
ORDER BY cities.id ASC;
