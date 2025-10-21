-- Affiche score et name de second_table en excluant les enregistrements sans nom
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
