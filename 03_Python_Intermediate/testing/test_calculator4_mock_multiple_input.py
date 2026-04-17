# Here we test user input and output of the main() function in calculator.py
# We use monkeypatch to mock input() and capsys to capture print() output.
# To run this test, use: pytest test_calculator4_mock_multiple_input.py 

import pytest
from calculator import main

@pytest.mark.parametrize("a,b,add_result,sub_result", [
    ("2", "3", "5.0", "-1.0"),
    ("-1", "1", "0.0", "-2.0"),
    ("0", "0", "0.0", "0.0"),
    ("2.5", "3.5", "6.0", "-1.0")
])

def test_main_multiple(monkeypatch, capsys, a, b, add_result, sub_result):
    
    inputs = iter([a, b])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert f"Addition: {add_result}" in captured.out
    assert f"Subtraction: {sub_result}" in captured.out

# sample output when running the test:
# ============ test session starts =========================
# platform win32 -- Python 3.11.9, pytest-9.0.3, pluggy-1.6.0
# rootdir: C:\Users\hi\Desktop\projects\python_projects\tutorial\tut_tensorflow\class\testing
# plugins: anyio-4.13.0
# collected 3 items                                                                                                                                                                                        

# test_calculator4_mock_multiple_input.py ...                                                                                                                                                        [100%]

# ============= 3 passed in 0.05s ======