import csv
import matplotlib.pyplot as plt

dates = []
distances = []
speeds = []

with open("data/processed/clean_rides.csv", "r") as file:
    reader = csv.DictReader(file)

    for ride in reader:
        dates.append(ride["date"])
        distances.append(float(ride["distance_km"]))
        speeds.append(float(ride["speed_kmh"]))


# График расстояния
plt.figure(figsize=(10, 5))
plt.plot(dates, distances, marker="o")

plt.title("Cycling Distance by Date")
plt.xlabel("Date")
plt.ylabel("Distance (km)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("data/processed/distance_by_date.png")

plt.show()

