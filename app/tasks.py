
def add_task(tasks, title):
    """Add a new task to the task list."""
    task = {
        "title": title,
        "completed": False,
    }
    tasks.append(task)


def list_tasks(tasks):
    """Return all tasks."""
    return tasks


def complete_task(tasks, index):
    """Mark a task as completed."""
    if index < 0 or index >= len(tasks):
        raise IndexError("Task index is out of range")

    tasks[index]["completed"] = True
