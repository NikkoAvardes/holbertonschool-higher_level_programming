#!/usr/bin/python3
"""Module for converting Python objects to JSON string representations.

This module provides functionality to serialize Python objects into JSON
string format using the standard json library for data interchange.
"""
import json


def to_json_string(my_obj):
    """Convert a Python object to its JSON string representation.
    
    This function takes any JSON-serializable Python object and returns
    its JSON string representation using the json.dumps() method.
    
    Args:
        my_obj: Any Python object that can be serialized to JSON
               (dict, list, str, int, float, bool, None).
               
    Returns:
        str: The JSON string representation of the input object.
        
    Raises:
        TypeError: If the object is not JSON serializable.
    """
    return json.dumps(my_obj)
