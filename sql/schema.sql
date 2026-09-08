CREATE TABLE rides (
    ride_id INTEGER PRIMARY KEY,
    date DATE,
    distance_km DECIMAL(10, 2),
    duration_min INTEGER,
    route VARCHAR(100),
    speed_kmh DECIMAL(10, 2)
);
