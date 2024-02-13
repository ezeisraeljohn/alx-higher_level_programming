-- List Number of records with the same score in a table
SELECT score, COUNT(*) AS number
From second_table
GROUP BY score
ORDER BY score DESC;
