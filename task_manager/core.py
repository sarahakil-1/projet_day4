import json
import os
from task_manager.logger import setup_logger
from task_manager.config import get_tasks_file_path

logger = setup_logger()
TASKS_FILE = get_tasks_file_path()

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Added task: {task}")
    return task

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['id']}: {task['description']} [Priority: {task['priority']}]")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        logger.warning(f"No task found with ID {task_id}")
        return False
    save_tasks(new_tasks)
    logger.info(f"Deleted task with ID {task_id}")
    return True

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.warning(f"Corrupted or empty tasks file: {TASKS_FILE}. Resetting to empty list.")
        return []
