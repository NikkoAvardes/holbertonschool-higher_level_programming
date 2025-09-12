#!/usr/bin/env python3
"""Module that contains add_integer function.

This module provides functionality for adding integers.

It includes type checking and conversion."""

def add_integer(a, b=98):
    """Adds 2 integers.
    
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
