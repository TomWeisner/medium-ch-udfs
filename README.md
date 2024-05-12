# medium-ch-udfs

This repo provides code and figures used in [this Medium story](https://medium.com/@tomweisner/user-defined-functions-in-clickhouse-with-python-c3f7724bd6de?source=friends_link&sk=806e2cab9eb4755746a358f11aa42c57)

## pre-reqs

- Linux OS
- python3
- A virtual environment
- Installed third party packages. See requirements.txt

## usage guide

simply execute src/plotActivity.py

this will generate data using src/data/generate.py

this will then be plotted as a base figure with src/data/plotGenerate.py

activity will then be identified with src/clickhouse/user_scripts/findActivity.py (which is the code used to define the UDF)

periods of activity will then be added to the base figure in src/plotActivity.py
