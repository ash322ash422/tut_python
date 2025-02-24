import datetime
import textwrap
from storage import save_tasks, load_tasks

def add_task(description):
    tasks = load_tasks()
    task = {
        "description": description,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: "{description}"')

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f'Removed task: "{removed_task["description"]}"')
    else:
        print("Invalid task number.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i}. {textwrap.shorten(task['description'], width=50)} - Created: {task['created_at']}")
