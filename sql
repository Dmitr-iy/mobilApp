SQL-запрос для поиска врачей, переместившихся более чем на 1 км за последние 10 минут:

SELECT d.name, l.latitude, l.longitude
FROM Doctors d
JOIN Locations l ON d.doctor_id = l.doctor_id
WHERE l.timestamp >= NOW() - INTERVAL 10 MINUTE
GROUP BY d.doctor_id
HAVING MAX(POWER(69.1 * (l.latitude - initial_latitude), 2) + POWER(69.1 * (initial_longitude - l.longitude) * COS(l.latitude / 57.3), 2)) > 1;


SQL-запрос для поиска врачей, у которых нет информации о перемещениях за последний час:

SELECT d.name
FROM Doctors d
LEFT JOIN Locations l ON d.doctor_id = l.doctor_id AND l.timestamp >= NOW() - INTERVAL 1 HOUR
WHERE l.location_id IS NULL;
