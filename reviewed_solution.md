```python
from typing import Union

def addition(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    This function adds two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y

def subtraction(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    This function subtracts two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The difference between x and y.
    """
    return x - y

import pytest

def test_addition_integers():
    assert addition(2, 3) == 5

def test_addition_floats():
    assert addition(2.5, 3.5) == 6.0

def test_subtraction_integers():
    assert subtraction(5, 2) == 3

def test_subtraction_floats():
    assert subtraction(5.5, 2.5) == 3.0

def test_addition_mixed_types():
    assert addition(2, 3.5) == 5.5

def test_subtraction_mixed_types():
    assert subtraction(5.5, 2) == 3.5

def test_addition_zero():
    assert addition(0,5) == 5
    assert addition(5,0) == 5

def test_subtraction_zero():
    assert subtraction(5,0) == 5
    assert subtraction(0,5) == -5

def test_addition_negative():
    assert addition(-2,3) == 1
    assert addition(2,-3) == -1

def test_subtraction_negative():
    assert subtraction(-2,3) == -5
    assert subtraction(2,-3) == 5

```