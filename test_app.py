import pytest
from app import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(4, 2) == 8
    assert multiply(0, 10) == 0
    assert multiply(-2, 3) == -6