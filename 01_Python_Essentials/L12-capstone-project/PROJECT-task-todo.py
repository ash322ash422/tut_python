
# Assignment 3: File-Based To-Do App
# This program demonstrates file handling, functions, loops, lists, and if-else
# Tasks are stored persistently in a text file

TASK_FILE = "tasks.txt"

# ---------------- FUNCTION 1: LOAD TASKS ----------------
def load_tasks():
    """
    Reads tasks from the file and returns them as a list.
    If file does not exist, returns an empty list.
    """
    tasks = []

    try:
        file = open(TASK_FILE, "r")
        for line in file:
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        # File does not exist yet, so return empty list
        tasks = []

    return tasks


# ---------------- FUNCTION 2: SAVE TASKS ----------------
def save_tasks(tasks):
    """
    Saves the list of tasks to the file.
    Each task is written on a new line.
    """
    file = open(TASK_FILE, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()


# ---------------- FUNCTION 3: ADD TASK ----------------
def add_task(tasks):
    """
    Adds a new task entered by the user.
    """
    task = input("Enter new task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# ---------------- FUNCTION 4: VIEW TASKS ----------------
def view_tasks(tasks):
    """
    Displays all tasks with numbering.
    """
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index in range(len(tasks)):
        print(index + 1, ".", tasks[index])


# ---------------- FUNCTION 5: DELETE TASK ----------------
def delete_task(tasks):
    """
    Deletes a task based on user-selected task number.
    """
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print("Deleted task:", removed_task)

    except ValueError:
        print("Please enter a valid number.")


# ---------------- MAIN PROGRAM ----------------

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()