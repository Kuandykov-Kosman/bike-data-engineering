from src.extract import extract_data


def transform_data(rides):
    clean_rides = []

    for ride in rides:
        ride["distance_km"] = float(ride["distance_km"])
        ride["duration_min"] = int(ride["duration_min"])

        ride["speed_kmh"] = round(
            ride["distance_km"] / (ride["duration_min"] / 60),
            2
        )

        clean_rides.append(ride)

    return clean_rides


if __name__ == "__main__":
    rides = extract_data()
    clean_rides = transform_data(rides)

    for ride in clean_rides:
        print(ride)
