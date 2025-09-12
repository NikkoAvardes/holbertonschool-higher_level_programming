#!/usr/bin/python3
"""Module that adds two integers.

This module contains a function that adds two integers or floats
after casting them to integers.
"""

def add_integer(a, b=98):
    """
    Adds 2 integers.
    
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
