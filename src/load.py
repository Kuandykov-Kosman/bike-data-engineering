import csv

from src.extract import extract_data
from src.transform import transform_data


def load_data(rides):
    with open(
        "data/processed/clean_rides.csv",
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "ride_id",
            "date",
            "distance_km",
            "duration_min",
            "route",
            "speed_kmh"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rides)


if __name__ == "__main__":
    rides = extract_data()
    clean_rides = transform_data(rides)

    load_data(clean_rides)

    print("Data loaded successfully!")
