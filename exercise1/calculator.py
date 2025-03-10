# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Returns the product of two numbers."""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """Returns the quotient of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b