SELECT competitor.name, 
MAX(CASE WHEN scores.round = 1 THEN scores.score END) AS round1,
MAX(CASE WHEN scores.round = 2 THEN scores.score END) AS round 2,
MAX(CASE WHEN scores.round = 3 THEN scores.score END) AS round 3
FROM competitor, scores
WHERE competitor.id = scores.id
GROUP BY competitor.name
ORDER BY competitor.name ASC;