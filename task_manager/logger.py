import logging
import os

def setup_logger(log_file="task_manager.log"):
    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)
    log_path = os.path.join(log_directory, log_file)

    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
