import os

def get_tasks_file_path():
    return os.getenv("TASKS_FILE_PATH", "tasks.json")
