# Budget Management System

A Python 3 terminal application for recording income and expenses, searching transactions, reviewing category reports, and tracking available balance.

## Run

From this directory, run `py main.py` (or `python main.py`). Data is stored automatically in `data/transactions.json`.

## Features

- Income and expense records with unique IDs, ISO dates, categories, and descriptions
- Search by type, category, exact date, and amount range
- Delete records after confirmation
- Income and spending breakdowns, totals, and available balance
- Automatic JSON directory creation, atomic saves, and graceful handling of missing, malformed, and legacy data

## Design

The application uses only Python's standard library. `Decimal` validates user-entered currency before converting it to integer minor units, avoiding floating-point arithmetic. Dataclasses represent transactions; UUIDs provide stable identifiers; JSON keeps data portable and human-readable. The CLI, validation, persistence, and report calculations live in separate modules to keep responsibilities clear.

## Project files

- `main.py`: menu and user interaction
- `model.py`: transaction model
- `validation.py`: amount, category, date, and selection validation
- `storage.py`: JSON loading, migration, and atomic persistence
- `summary.py`: totals and balances
- `reports.py`: transaction filtering
- `tests/`: unit tests
