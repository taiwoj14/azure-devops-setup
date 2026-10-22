# Azure DevOps Setup Mini-Project

## Overview

This project demonstrates a Python task-management application with automated testing using Azure Pipelines.

## Application Features

- Add a task to a task list.
- List existing tasks.
- Mark a task as completed.
- Validate task indexes when completing tasks.

## Project Structure

- `app/tasks.py` - Application functions.
- `tests/test_tasks.py` - Automated tests.
- `requirements.txt` - Python dependencies.
- `azure-pipelines.yml` - Azure Pipelines configuration.

## Run Locally

1. Create a virtual environment using `python3 -m venv .venv`.
2. Activate it using `source .venv/bin/activate`.
3. Install dependencies using `python -m pip install -r requirements.txt`.
4. Run the tests using `python -m pytest -v`.

## Continuous Integration

The Azure Pipeline uses Python 3.12, installs project dependencies, and runs the automated test suite when changes are pushed to the main branch.
