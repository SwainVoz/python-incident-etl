# Python Incident Analysis ETL

A small Python ETL pipeline for analyzing incident records.

## What it does

The pipeline reads incident records from a CSV file, validates that durations
are non-negative integers, counts valid and invalid records, aggregates valid
incidents by service, and totals the duration of resolved incidents. It writes
the resulting report as JSON.

## Technologies

Python, CSV, JSON, pytest, and uv.

## Run

From the project directory:

```sh
uv sync
uv run python incidents.py
uv run pytest -v
```

The default run reads `incidents.csv` and writes `report.json`.

## Tests

The test suite contains six automated pytest tests covering valid, invalid,
empty, multiple, negative-duration, and JSON-output cases.
