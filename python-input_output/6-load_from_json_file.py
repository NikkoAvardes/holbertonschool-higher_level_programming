#!/usr/bin/python3
"""Module for loading Python objects from JSON files.

This module provides functionality to read JSON files and deserialize them
into their corresponding Python objects for data processing and manipulation.
"""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file.
    
    This function reads a JSON file and deserializes its contents into
    the corresponding Python object using the json.load() method.
    
    Args:
        filename (str): The path to the JSON file to be loaded.
                       
    Returns:
        object: The Python object represented by the JSON file contents
               (dict, list, str, int, float, bool, None).
               
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        IOError: If there are issues reading the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
