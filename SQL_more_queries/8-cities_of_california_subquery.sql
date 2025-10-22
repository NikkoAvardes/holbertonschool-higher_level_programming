-- Liste toutes les villes de Californie en utilisant une sous-requête (sans JOIN)
SELECT cities.name
FROM cities
WHERE cities.id IN (
	SELECT id FROM states WHERE name = "California"
)
ORDER BY cities.id ASC;
