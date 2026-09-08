import csv


def extract_data():
    with open("data/raw/rides.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    rides = extract_data()

    print(f"Loaded {len(rides)} rides")

    for ride in rides:
        print(ride)
