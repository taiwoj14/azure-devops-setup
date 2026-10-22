import pytest

from app.tasks import add_task, list_tasks, complete_task


def test_add_task():
    tasks = []
    add_task(tasks, "Learn Azure DevOps")

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn Azure DevOps"
    assert tasks[0]["completed"] is False


def test_list_tasks():
    tasks = [
        {"title": "Learn Python", "completed": False},
        {"title": "Learn Azure", "completed": True},
    ]

    result = list_tasks(tasks)

    assert len(result) == 2


def test_complete_task():
    tasks = [{"title": "Build a pipeline", "completed": False}]

    complete_task(tasks, 0)

    assert tasks[0]["completed"] is True


def test_complete_task_invalid_index():
    tasks = [{"title": "Build a pipeline", "completed": False}]

    with pytest.raises(IndexError, match="Task index is out of range"):
        complete_task(tasks, 1)
