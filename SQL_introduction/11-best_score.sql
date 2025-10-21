-- Affiche les enregistrements avec score >= 10, triés par score décroissant
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
