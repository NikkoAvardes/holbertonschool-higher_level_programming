#!/usr/bin/python3
"""Module for saving Python objects to JSON files.

This module provides functionality to serialize Python objects and save them
to files in JSON format for persistent storage and data exchange.
"""
import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a file in JSON format.

    This function serializes a Python object to JSON and writes it to a file.
    The file is created or overwritten with the JSON representation of the
    object.

    Args:
        my_obj: Any JSON-serializable Python object to be saved
               (dict, list, str, int, float, bool, None).
        filename (str): The path to the file where the JSON data will be saved.

    Returns:
        None: This function performs file I/O and returns nothing.

    Raises:
        TypeError: If the object is not JSON serializable.
        IOError: If there are issues writing to the file.
        PermissionError: If there are insufficient permissions to write
                        the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
