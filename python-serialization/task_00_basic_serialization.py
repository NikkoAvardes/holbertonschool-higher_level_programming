#!/usr/bin/env python3
"""
Basic serialization module for JSON operations.

This module provides functionality to serialize Python dictionaries to JSON
files and deserialize JSON files back to Python dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and save data to a JSON file.

    Args:
        data (dict): A Python dictionary with data to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, "r", encoding='utf-8') as e:
        koko = json.load(e)
        return koko
