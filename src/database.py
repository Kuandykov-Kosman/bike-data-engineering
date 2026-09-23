import sqlite3
import csv


DATABASE_PATH = "data/database/bike_rides.db"
CSV_PATH = "data/processed/clean_rides.csv"


def create_database():
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rides (
            ride_id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            distance_km REAL NOT NULL,
            duration_min INTEGER NOT NULL,
            route TEXT NOT NULL,
            speed_kmh REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def load_data():
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    with open(CSV_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)

        for ride in reader:
            cursor.execute(
                """
                INSERT OR REPLACE INTO rides
                (ride_id, date, distance_km, duration_min, route, speed_kmh)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    int(ride["ride_id"]),
                    ride["date"],
                    float(ride["distance_km"]),
                    int(ride["duration_min"]),
                    ride["route"],
                    float(ride["speed_kmh"])
                )
            )

    connection.commit()
    connection.close()


def main():
    create_database()
    load_data()
    print("Data loaded into SQLite successfully!")


if __name__ == "__main__":
    main()
