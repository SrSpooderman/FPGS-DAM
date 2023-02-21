SELECT p.NAME, s.GOALS AS goles, s.MATCHES
FROM PLAYERS p
JOIN STATS s ON p.STAT_ID = s.STAT_ID
WHERE goles > 1 AND MATCHES BETWEEN 20 AND 28
ORDER BY s.MATCHES DESC;