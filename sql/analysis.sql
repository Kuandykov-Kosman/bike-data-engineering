-- Средняя дистанция поездки
SELECT AVG(distance_km) AS average_distance
FROM rides;

-- Средняя скорость
SELECT AVG(speed_kmh) AS average_speed
FROM rides;

-- Самая длинная поездка
SELECT *
FROM rides
ORDER BY distance_km DESC
LIMIT 1;

-- Самая быстрая поездка
SELECT *
FROM rides
ORDER BY speed_kmh DESC
LIMIT 1;

-- Общее расстояние
SELECT SUM(distance_km) AS total_distance
FROM rides;

-- Количество поездок
SELECT COUNT(*) AS total_rides
FROM rides;
