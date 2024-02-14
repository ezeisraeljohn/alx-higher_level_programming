-- Find Max temperatures based on cities
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
