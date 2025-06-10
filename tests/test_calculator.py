import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -7) == -12

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(-5, 3) == -8

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0
    assert multiply(-4, -5) == 20

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5
    assert divide(-10, -2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by Zero"):
        divide(1, 0)