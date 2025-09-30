#!/usr/bin/python3
"""Module for converting class instances to JSON-serializable dictionaries.

This module provides functionality to extract the dictionary representation
of class instances, making them suitable for JSON serialization by returning
their __dict__ attribute which contains all instance variables.
"""


def class_to_json(obj):
    """Return the dictionary representation of a class instance.
    
    This function extracts the __dict__ attribute from any class instance,
    which contains all the instance variables as a dictionary. This dictionary
    can then be easily serialized to JSON format.
    
    Args:
        obj: Any class instance that has a __dict__ attribute containing
            serializable data types (list, dict, str, int, bool).
            
    Returns:
        dict: A dictionary containing all instance variables and their values
             from the object's __dict__ attribute.
             
    Note:
        The returned dictionary will only contain simple data structures
        that are JSON serializable (list, dict, str, int, bool).
    """
    return obj.__dict__
