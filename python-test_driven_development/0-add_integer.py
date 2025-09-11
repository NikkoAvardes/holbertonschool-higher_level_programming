#!/usr/bin/env python3
"""Module that contains add_integer function"""

def add_integer(a, b=98):
    """
    Adds 2 integers.
    
    Args:
        a: first integer (int or float)
        b: second integer (int or float), defaults to 98
    
    Returns:
        int: sum of a and b as integers
    
    Raises:
        TypeError: if a is not int or float
        TypeError: if b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
