import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", help="Description of the task")
    parser_add.add_argument("priority", type=int, help="Priority of the task")

    # List Command
    subparsers.add_parser("list", help="List all tasks")

    # Delete Command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.description, args.priority)
        print(f"Task added: {task}")
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        success = delete_task(args.id)
        if success:
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task {args.id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
