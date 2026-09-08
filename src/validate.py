from extract import extract_data


def validate_data(rides):
    errors = []

    for ride in rides:
        if float(ride["distance_km"]) <= 0:
            errors.append(
                f"Ride {ride['ride_id']}: invalid distance"
            )

        if int(ride["duration_min"]) <= 0:
            errors.append(
                f"Ride {ride['ride_id']}: invalid duration"
            )

    return errors


if __name__ == "__main__":
    rides = extract_data()
    errors = validate_data(rides)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(error)
    else:
        print("Validation passed!")
