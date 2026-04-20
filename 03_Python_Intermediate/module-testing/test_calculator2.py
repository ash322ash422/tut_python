# This file contains tests for the add_numbers function in calculator.py
# To run the tests, use the command: pytest test_calculator2.py

import pytest
from calculator import add_numbers

# Best Feature: Parameterized Testing
# Instead of writing multiple test functions, we write one and feed multiple inputs”
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 3.5, 6.0)
])

def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected

# Edge Case Testing
def test_large_numbers():
    assert add_numbers(1_000_000, 2_000_000) == 3_000_000

# > pytest test_calculator2.py
# ============== test session starts ===========================
# platform win32 -- Python 3.11.9, pytest-9.0.3, pluggy-1.6.0
# rootdir: C:\Users\hi\Desktop\projects\python_projects\tutorial\tut_tensorflow\class\testing
# plugins: anyio-4.13.0
# collected 5 items                                                                                                                                                                                        

# test_calculator2.py .....                                                                                                                                                                          [100%]

# ================ 5 passed in 0.06s ===========================
