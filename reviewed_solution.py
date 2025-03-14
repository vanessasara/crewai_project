```python
from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y

def sub(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Subtracts two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The difference between x and y.
    """
    return x - y


import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, 1, 0),
    (0,0,0),
    (1.5,2.5,4.0)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 1, 1),
    (10, 5, 5),
    (1,-1,2),
    (0,0,0),
    (2.5,1.5,1.0)
])
def test_sub(x, y, expected):
    assert sub(x, y) == expected

def test_add_large_numbers():
    assert add(10**10, 10**10) == 2 * 10**10

```