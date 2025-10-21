-- Groupe les enregistrements par score et compte le nombre d'occurrences de chaque score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
