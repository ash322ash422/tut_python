import shutil
import os

def clear_screen():
    """Clears the terminal screen."""
    shutil.get_terminal_size()  # Just to demonstrate shutil usage
    os.system('cls' if os.name == 'nt' else 'clear')
