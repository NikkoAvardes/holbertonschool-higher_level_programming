#!/usr/bin/env python3
"""
CSV to JSON conversion module.

This module provides functionality to convert CSV files to JSON format
using Python's csv and json modules for data serialization.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert a CSV file to JSON format.

    Reads data from a CSV file using DictReader and converts it to JSON format.
    The resulting JSON data is saved to 'data.json' file.

    Args:
        csv_file (str): The filename of the input CSV file to convert.

    Returns:
        bool: True if conversion was successful, False if file not found.
    """
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False
