SELECT competitor.name, scores.score
FROM competitor, scores
WHERE competitor.id = scores.id and scores.round = ?

