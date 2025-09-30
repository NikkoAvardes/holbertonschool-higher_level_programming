#!/usr/bin/python3
"""Module for converting JSON strings to Python objects.

This module provides functionality to deserialize JSON string representations
into their corresponding Python objects using the standard json library.
"""
import json


def from_json_string(my_str):
    """Convert a JSON string to its corresponding Python object.

    This function takes a valid JSON string and returns the corresponding
    Python object using the json.loads() method for deserialization.

    Args:
        my_str (str): A valid JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string
               (dict, list, str, int, float, bool, None).

    Raises:
        json.JSONDecodeError: If the string is not valid JSON.
        TypeError: If the input is not a string.
    """
    return json.loads(my_str)
