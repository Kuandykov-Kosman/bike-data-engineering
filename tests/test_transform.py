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
