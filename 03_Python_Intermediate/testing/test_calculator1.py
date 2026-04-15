# NOTE: file name must be test_*.py
# To run the all tests, use  : pytest test_calculator1.py
# To run a specific test, use: pytest -k "test_add_numbers" test_calculator1.py

from calculator import add_numbers, subtract_numbers

# Note: function name must start with test_ to be recognized by pytest
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(3, 5) == -2
    assert subtract_numbers(0, 0) == 0


# sample run output:
# > pytest test_calculator1.py                      
# =========== test session starts =============================
# platform win32 -- Python 3.11.9, pytest-9.0.3, pluggy-1.6.0
# rootdir: C:\Users\hi\Desktop\projects\python_projects\tutorial\tut_tensorflow\class\testing
# plugins: anyio-4.13.0
# collected 2 items                                                                                                                                                                                    

# test_calculator1.py ..                                                                                                                                                                         [100%]

# ========== 2 passed in 0.06s ===============
