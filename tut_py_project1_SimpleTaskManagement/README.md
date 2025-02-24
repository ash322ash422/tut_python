# Personal Task Manager - Python Project

This simple **Personal Task Manager** project demonstrates the use of Python's built-in libraries to manage a task list with functionalities to add, remove, and list tasks. It uses modules such as `argparse`, `json`, `datetime`, `textwrap`, and `os` to handle various aspects like file operations, date management, text processing, and user input handling. It also shows time taken to finish the task.

## File Structure

The project is organized as follows:

task_manager/ 

|── main.py # Entry point of the application. Manages user input and triggers actions. 

│── task_handler.py # Logic for adding, removing, and listing tasks. 

│── storage.py # File operations for saving and loading tasks to/from a JSON file. 

│── utils.py # Helper functions for additional utilities (like clearing terminal). 

│── tasks.json # Storage file where tasks are saved (auto-created if not present).


## Key Features and Libraries

1. **Adding Tasks**: Use `--add` to add a new task with a description.
2. **Listing Tasks**: Use `--list` to view all saved tasks with their descriptions and timestamps.
3. **Removing Tasks**: Use `--remove` followed by the task number to remove a task.

The project uses the following Python built-in libraries:
- **`argparse`**: To handle command-line arguments and provide functionality for adding, removing, and listing tasks.
- **`datetime`**: To store timestamps when tasks are created.
- **`json`**: To save tasks in a JSON file for persistent storage.
- **`textwrap`**: To format and shorten task descriptions when listing tasks.
- **`os`**: To handle system-related operations (e.g., checking for file existence).
- **`shutil`**: To clear the terminal screen as a utility function.

## Key Takeaways for Students

- **File Handling**: Learn how to use the `json` module to read and write data to files.
- **Date Handling**: Use the `datetime` module to capture timestamps for tasks and format them appropriately.
- **Command-line Interaction**: Understand how to use the `argparse` module for handling user input and making the application interactive.
- **Text Processing**: Learn how to process and format strings using `textwrap` for clean task listings.
- **System Operations**: Explore the `os` and `shutil` modules to perform system-related tasks such as file checking and clearing the terminal screen.

## How to Run the Project

1. **Clone the repository** to your local machine or work in Jupyter Notebook.
2. Open a terminal in the project folder and run the following commands:
   
   - To add a new task:
     ```bash
     python main.py --add "Complete Python assignment"
     ```

   - To list all tasks:
     ```bash
     python main.py --list
     ```

   - To remove a task (e.g., task number 0):
     ```bash
     python main.py --remove 0
     ```

3. Check the `tasks.json` file to see the tasks being saved.

## Conclusion

This project provides a hands-on approach to understanding basic Python libraries and their real-world applications. It covers multiple Python modules and demonstrates how they can be combined to create a useful tool. It's perfect for teaching beginner-level students about file handling, command-line arguments, and task automation.

