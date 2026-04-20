# Here we test user input and output of the main() function in calculator.py
# We use monkeypatch to mock input() and capsys to capture print() output.
# To run this test, use: pytest test_calculator3_mock_input.py

import pytest
from calculator import main

def test_main(monkeypatch, capsys):
    
    # Step 1: Mock input()
    inputs = iter(["10", "5"])  # simulate user typing
    
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    # Step 2: Run main()
    main()
    
    # Step 3: Capture output
    captured = capsys.readouterr()
    
    # Step 4: Assertions
    assert "Addition: 15.0" in captured.out
    assert "Subtraction: 5.0" in captured.out

# sample output when running pytest:
# ============ test session starts =================================
# platform win32 -- Python 3.11.9, pytest-9.0.3, pluggy-1.6.0
# rootdir: C:\Users\hi\Desktop\projects\python_projects\tutorial\tut_tensorflow\class\testing
# plugins: anyio-4.13.0
# collected 1 item                                                                                                                                                                                         

# test_calculator3_mock_input.py .                                                                                                                                                                   [100%]

# ============ 1 passed in 0.04s ==========