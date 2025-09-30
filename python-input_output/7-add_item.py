#!/usr/bin/python3
"""Script for adding command line arguments to a JSON file list.

This script maintains a persistent list stored in a JSON file and allows
adding new items to the list through command line arguments. The list is
loaded from the file if it exists, new arguments are appended, and the
updated list is saved back to the file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list from file or create empty list if file doesn't exist
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])
# Save the updated list back to the file
save_to_json_file(my_list, filename)
