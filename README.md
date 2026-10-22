# Azure DevOps Setup Mini-Project

## 1. Project Overview

This project demonstrates a Python task-management application with an automated Continuous Integration (CI) pipeline built using Azure DevOps.

The pipeline is configured to run automatically when changes are pushed to the `main` branch. It installs the Python dependencies, executes automated tests, publishes individual test results, and reports code coverage.

The project also demonstrates how a CI pipeline detects a test failure and returns to a successful state after the problem is fixed.

## 2. Project Objectives

- Store and manage application code using Git and Azure Repos.
- Configure an Azure Pipeline using YAML.
- Automate Python dependency installation and unit testing.
- Trigger pipeline runs automatically when code is pushed to `main`.
- Publish test results and code coverage reports in Azure DevOps.
- Practise troubleshooting through a controlled test failure and recovery.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Azure Repos | Source code version control |
| Azure Pipelines | Automated CI workflow |
| Git | Source control and change management |
| Python 3.12 | Application and test execution |
| pytest | Automated unit testing |
| pytest-cov | Code coverage measurement |
| YAML | Pipeline configuration |
| Ubuntu hosted agent | Pipeline execution environment |

## 4. Application Features

The task-management application supports:

- Adding tasks to a task list.
- Listing existing tasks.
- Marking tasks as completed.
- Handling invalid task indexes when completing a task.

## 5. Project Structure

```text
azure-devops-setup/
├── app/
│   ├── __init__.py
│   └── tasks.py
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
├── screenshots/
│   ├── 4-passed tests.png
│   ├── azure-code-coverage-100-percent.png
│   ├── azure-devops-tests-summary.png
│   ├── azure-pipeline-failure-recovery.png
│   ├── azure-pipelines-successful.png
│   └── azure-repos-files.png
├── .gitignore
├── azure-pipelines.yml
├── README.md
└── requirements.txt
```

## 6. Run the Project Locally

### Prerequisites

- Python 3.12 or a compatible Python 3 installation
- Git
- Visual Studio Code or another code editor

### Create and activate a virtual environment

From the project directory, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the automated tests

```bash
python -m pytest -v
```

The current test suite contains four tests.

### Generate test results and code coverage locally

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-report=xml:coverage.xml --junitxml=test-results.xml
```

This command runs the tests, displays code coverage in the terminal, and generates XML reports for test results and coverage.

## 7. Azure Pipelines CI Workflow

The pipeline configuration is stored in `azure-pipelines.yml`.

The workflow performs the following steps:

1. **Trigger:** Starts automatically when changes are pushed to `main`.
2. **Agent setup:** Uses a Microsoft-hosted Ubuntu agent.
3. **Python setup:** Selects Python 3.12.
4. **Dependency installation:** Installs the packages listed in `requirements.txt`.
5. **Automated testing:** Runs the pytest test suite.
6. **Test reporting:** Publishes the JUnit test-results report to Azure DevOps.
7. **Code coverage:** Publishes the coverage report to Azure DevOps.

### Pipeline-generated reports

| Report | Purpose |
|---|---|
| `test-results.xml` | Publishes individual test outcomes |
| `coverage.xml` | Provides code coverage data |

Both generated XML files are excluded from Git using `.gitignore`.

## 8. Automated Tests

The project includes the following tests:

| Test | Purpose |
|---|---|
| `test_add_task` | Verifies that a task can be added |
| `test_list_tasks` | Verifies task-list functionality |
| `test_complete_task` | Verifies that a task can be marked completed |
| `test_complete_task_invalid_index` | Verifies handling of an invalid task index |

### Verified results

The four-test suite passed locally and in Azure Pipelines after the failure-recovery exercise.

## 9. Code Coverage

The project uses `pytest-cov` to measure statement coverage for the `app` package.

**Verified result for `app/tasks.py`:**

- Statements: 9
- Missed statements: 0
- Statement coverage: 100%

This result applies to the measured application statements in `app/tasks.py`; it does not imply that every possible execution path or branch has been tested.

Azure Pipelines publishes the generated coverage report so the result can be inspected in the Code Coverage tab of a pipeline run.

## 10. CI Failure and Recovery Demonstration

A controlled experiment was used to understand how CI detects test failures.

1. A temporary test containing an intentionally false assertion was added.
2. The local test run showed one failure while the original four tests passed.
3. The change was pushed to Azure Repos.
4. Azure Pipelines detected the failure and marked the run as failed.
5. The temporary test was removed.
6. The four-test suite was run again, and all four tests passed.
7. The fix was pushed, and the subsequent Azure Pipeline run succeeded.

The temporary failing test has been removed from the final test suite.

## 11. Screenshots and Evidence

The `screenshots/` folder contains evidence of the project's implementation and results.

| Evidence | Screenshot |
|---|---|
| Repository files | [View screenshot](screenshots/azure-repos-files.png) |
| Successful pipeline run | [View screenshot](screenshots/azure-pipelines-successful.png) |
| Four passing tests in the terminal | [View screenshot](screenshots/4-passed%20tests.png) |
| Azure DevOps test summary | [View screenshot](screenshots/azure-devops-tests-summary.png) |
| 100% statement coverage | [View screenshot](screenshots/azure-code-coverage-100-percent.png) |
| Pipeline failure and recovery | [View screenshot](screenshots/azure-pipeline-failure-recovery.png) |

## 12. Key Learning Outcomes

Through this project, I practised:

- Managing source code with Git and Azure Repos.
- Writing and maintaining a YAML-based CI pipeline.
- Configuring automatic pipeline triggers.
- Running and interpreting automated test results.
- Publishing test results and code coverage reports.
- Investigating a failed pipeline and verifying recovery after a fix.
- Documenting project implementation with screenshots.

## 13. Scope and Future Improvements

This project currently demonstrates Continuous Integration, automated testing, and reporting. It does not yet implement application deployment.

Possible future improvements include adding a deployment stage, expanding the test suite, and introducing additional quality checks.

---

**Project:** Azure DevOps Setup Mini-Project

**Repository:** Azure-DevOps-Setup