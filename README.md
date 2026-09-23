Bike Data Engineering 🚴

A beginner Data Engineering project for processing, validating, storing, 
analyzing, and visualizing bicycle ride data.

Project Goal

The goal of this project is to build a complete data pipeline that takes 
raw cycling data and turns it into clean, validated, structured, and 
analyzable data.

The project demonstrates fundamental Data Engineering concepts:

* Data extraction
* Data validation
* Data transformation
* Data loading
* Database storage
* SQL analysis
* Automated testing
* Data visualization
* Pipeline automation

Architecture

Raw CSV
   ↓
Extract
   ↓
Validate
   ↓
Transform
   ↓
Processed CSV
   ↓
SQLite Database
   ↓
SQL Analysis
   ↓
Visualizations

The entire pipeline can also be executed with one command:

python run_pipeline.py

Technologies

* Python 3
* SQLite
* SQL
* CSV
* pytest
* Matplotlib
* Git
* GitHub

Project Structure

bike-data-engineering/
│
├── data/
│   ├── raw/
│   │   └── rides.csv
│   │
│   ├── processed/
│   │   ├── clean_rides.csv
│   │   ├── distance_by_date.png
│   │   ├── speed_by_date.png
│   │   └── duration_by_date.png
│   │
│   └── database/
│       └── bike_rides.db
│
├── src/
│   ├── _init_.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── database.py
│   └── visualize.py
│
├── sql/
│   ├── schema.sql
│   ├── analysis.sql
│   └── sqlite_analysis.sql
│
├── tests/
│   └── test_transform.py
│
├── run_pipeline.py
├── pytest.ini
├── .gitignore
└── README.md

Dataset

The raw dataset contains bicycle rides with the following fields:

Field	Description
ride_id	Unique ride identifier
date	Date of the ride
distance_km	Distance in kilometers
duration_min	Ride duration in minutes
route	Ride route
speed_kmh	Calculated average speed

The project currently uses 10 sample cycling rides.

ETL Pipeline

1. Extract

src/extract.py

Reads raw cycling data from:

data/raw/rides.csv

The CSV data is loaded into Python for further processing.

2. Validate

src/validate.py

Checks that:

* Distance is greater than 0
* Duration is greater than 0

The pipeline stops if validation fails.

3. Transform

src/transform.py

Converts the raw values into appropriate data types and calculates average 
cycling speed.

The calculated speed is:

speed = distance / time

4. Load

src/load.py

Saves the transformed data into:

data/processed/clean_rides.csv

5. Database

src/database.py

Loads the processed data into a SQLite database:

data/database/bike_rides.db

The database contains a rides table.

SQL Analysis

SQL queries are stored in:

sql/sqlite_analysis.sql

The analysis includes:

* Average distance
* Average speed
* Total distance
* Total number of rides
* Longest ride
* Fastest ride

Example result from the current dataset:

Average distance: 27.23 km
Average speed: 19.269 km/h
Total distance: 272.3 km
Total rides: 10

Data Visualization

The project generates three visualizations:

* Distance by date
* Speed by date
* Duration by date

Generated files are stored in:

data/processed/

Testing

The project uses pytest.

Run the tests with:

pytest

Current test suite:

6 passed

The tests check:

* Speed calculation
* Data types
* Speed calculation with different values
* Speed rounding
* Multiple rides
* Distance conversion to float

Running the Project

Activate the virtual environment:

source .venv/bin/activate

Run the complete pipeline:

python run_pipeline.py

Run tests:

pytest

Future Improvements

Planned improvements include:

* More realistic cycling datasets
* More advanced data validation
* Additional SQL analysis
* PostgreSQL
* Docker
* Apache Airflow
* Automated scheduled pipelines
* Interactive dashboard
* Larger datasets
* Cloud data storage

Author

This project was created as a learning and portfolio project to practice 
Data Engineering fundamentals.
