#!/usr/bin/python3
"""Module that adds two integers.

This module contains a function that adds two integers or floats
after casting them to integers.
"""


def add_integer(a, b=98):
    """Adds 2 integers.
    
    """
    # Check for NaN values
    if (isinstance(a, float) and a != a) or (isinstance(b, float) and b != b):
        raise ValueError("cannot convert float NaN to integer")
    
    # Check for infinity values
    if (isinstance(a, float) and (a == float('inf') or a == float('-inf'))) or \
       (isinstance(b, float) and (b == float('inf') or b == float('-inf'))):
        raise OverflowError("cannot convert float infinity to integer")
    
    # Check type validation
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
