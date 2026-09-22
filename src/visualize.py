import csv
import matplotlib.pyplot as plt

dates = []
distances = []
speeds = []
durations = []

with open("data/processed/clean_rides.csv", "r") as file:
    reader = csv.DictReader(file)

    for ride in reader:
        dates.append(ride["date"])
        distances.append(float(ride["distance_km"]))
        speeds.append(float(ride["speed_kmh"]))
        durations.append(int(ride["duration_min"]))


# График расстояния
plt.figure(figsize=(10, 5))
plt.plot(dates, distances, marker="o")

plt.title("Cycling Distance by Date")
plt.xlabel("Date")
plt.ylabel("Distance (km)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("data/processed/distance_by_date.png")
plt.close()


# График скорости
plt.figure(figsize=(10, 5))
plt.plot(dates, speeds, marker="o")

plt.title("Cycling Speed by Date")
plt.xlabel("Date")
plt.ylabel("Speed (km/h)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("data/processed/speed_by_date.png")
plt.close()


# График длительности
plt.figure(figsize=(10, 5))
plt.plot(dates, durations, marker="o")

plt.title("Cycling Duration by Date")
plt.xlabel("Date")
plt.ylabel("Duration (minutes)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("data/processed/duration_by_date.png")
plt.close()

print("Visualizations created successfully!")

