from src.transform import transform_data


def test_speed_calculation():
    rides = [
        {
            "ride_id": "1",
            "date": "2026-08-01",
            "distance_km": "30",
            "duration_min": "60",
            "route": "Astana"
        }
    ]

    result = transform_data(rides)

    assert result[0]["speed_kmh"] == 30.0


def test_data_types():
    rides = [
        {
            "ride_id": "1",
            "date": "2026-08-01",
            "distance_km": "25.5",
            "duration_min": "60",
            "route": "Astana"
        }
    ]

    result = transform_data(rides)

    assert isinstance(result[0]["distance_km"], float)
    assert isinstance(result[0]["duration_min"], int)


def test_speed_with_different_values():
    rides = [
        {
            "ride_id": "1",
            "date": "2026-08-01",
            "distance_km": "20",
            "duration_min": "30",
            "route": "Astana"
        }
    ]

    result = transform_data(rides)

    assert result[0]["speed_kmh"] == 40.0


def test_speed_rounding():
    rides = [
        {
            "ride_id": "1",
            "date": "2026-08-01",
            "distance_km": "10",
            "duration_min": "30",
            "route": "Astana"
        }
    ]

    result = transform_data(rides)

    assert result[0]["speed_kmh"] == 20.0


def test_multiple_rides():
    rides = [
        {
            "ride_id": "1",
            "date": "2026-08-01",
            "distance_km": "30",
            "duration_min": "60",
            "route": "Astana"
        },
        {
            "ride_id": "2",
            "date": "2026-08-02",
            "distance_km": "20",
            "duration_min": "60",
            "route": "Astana"
        }
    ]

    result = transform_data(rides)

    assert len(result) == 2
    assert result[0]["speed_kmh"] == 30.0
    assert result[1]["speed_kmh"] == 20.0


def test_distance_is_float():
    rides = [
        {
            "ride_id": "1",
            "date": "2026-08-01",
            "distance_km": "42.5",
            "duration_min": "100",
            "route": "Astana"
        }
    ]

    result = transform_data(rides)

    assert isinstance(result[0]["distance_km"], float)
