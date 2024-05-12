# medium-ch-udfs

This repo provides code and figures used in [this Medium story](https://medium.com/@tomweisner/user-defined-functions-in-clickhouse-with-python-c3f7724bd6de?source=friends_link&sk=806e2cab9eb4755746a358f11aa42c57)

## Pre-reqs

- Linux OS
- python3
- A virtual environment
- Installed third party packages. See requirements.txt

## Usage guide

Simply execute src/plotActivity.py

This will generate data using src/data/generate.py

Data will then be plotted as a base figure with src/data/plotGenerate.py

Activity will then be identified with src/clickhouse/user_scripts/findActivity.py (which is the python code used to define the UDF)

Periods of activity will then be added to the base figure in src/plotActivity.py
