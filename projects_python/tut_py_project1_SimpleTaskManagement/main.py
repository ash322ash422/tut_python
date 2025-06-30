import argparse
import time
from task_handler import add_task, remove_task, list_tasks

def main():
    # Record the start time
    start_time = time.time()

    parser = argparse.ArgumentParser(description="Simple Task Manager using Python Native Libraries")
    parser.add_argument("--add", metavar='"Task Description"', help="Add a new task")
    parser.add_argument("--remove", metavar="Task Number", type=int, help="Remove a task by its number")
    parser.add_argument("--list", action="store_true", help="List all tasks")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.remove is not None:
        remove_task(args.remove)
    elif args.list:
        list_tasks()
    else:
        print("Use --help to see available commands.")

    # Calculate the time taken
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\nTask completed in {time_taken:.2f} seconds.")

if __name__ == "__main__":
    main()
