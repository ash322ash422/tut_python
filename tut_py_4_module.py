"""
What is a Module in Python?

A module in Python is a file containing Python code (functions, classes, and variables) that can be imported and used in other Python scripts.

A module helps in code organization and reusability, allowing developers to break large programs into smaller, manageable parts.


Why Do We Need Modules?
1. Code Reusability – Write once, use multiple times.
2. Maintainability – Easier to debug and update.
3. Organization – Keeps code structured.
4. Namespace Management – Avoids naming conflicts by keeping code separate.


Types of Modules in Python
1. Built-in Modules (e.g., math, random, os)
2. User-Defined Modules (as shown below)
3. Third-Party Modules (installed via pip, e.g., numpy, pandas)

Library is A collection of modules
"""

import tut_py_4_module_math_utils as utils

print(utils.add(5, 3))        # Output: 8
print(utils.subtract(10, 4))  # Output: 6
print(utils.PI)               # Output: 3.14159
