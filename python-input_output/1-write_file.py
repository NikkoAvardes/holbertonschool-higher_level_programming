#!/usr/bin/python3
"""Module for writing text content to files.

This module provides functionality to write text data to files with UTF-8
encoding, replacing any existing content in the target file.
"""


def write_file(filename="", text=""):
    """Write text content to a file, replacing existing content.

    This function creates or overwrites a file with the provided text content.
    The file is written using UTF-8 encoding to ensure proper character
    handling.

    Args:
        filename (str): The path to the file where text will be written.
                       Defaults to empty string.
        text (str): The text content to write to the file.
                   Defaults to empty string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If there are issues writing to the file.
        PermissionError: If there are insufficient permissions to write
                        the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
