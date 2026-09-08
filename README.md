# Bike Data Engineering

A small Data Engineering project for processing bicycle ride data.

## Project Goal

Build an ETL pipeline that extracts, validates, transforms and loads bicycle ride data.

## Architecture

CSV
↓
Extract
↓
Validate
↓
Transform
↓
Load
↓
Processed CSV
↓
SQL Analysis

## Technologies

- Python 3
- CSV
- SQL
- PostgreSQL
- pytest
- Git

## Project Structure

bike-data-engineering/
├── data/
│   ├── raw/
│   │   └── rides.csv
│   └── processed/
│       └── clean_rides.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   └── load.py
├── sql/
│   ├── schema.sql
│   └── analysis.sql
├── tests/
│   └── test_transform.py
├── .gitignore
└── README.md

## ETL Pipeline

### Extract

Reads raw bicycle ride data from a CSV file.

### Validate

Checks that distance and duration contain valid positive values.

### Transform

Converts data types and calculates average speed.

### Load

Saves transformed data to a processed CSV file.

## Tests

Run:

pytest

Expected result:

2 passed

## Data

The dataset contains bicycle rides with:

- ride ID
- date
- distance
- duration
- route
- average speed

## Future Improvements

- PostgreSQL database
- Docker
- Apache Airflow
- More realistic cycling data
- Automated ETL pipeline
- Data visualization
