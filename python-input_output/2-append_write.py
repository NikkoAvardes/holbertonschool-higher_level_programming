#!/usr/bin/python3
"""Module for appending text content to files.

This module provides functionality to append text data to the end of existing
files or create new files if they don't exist, using UTF-8 encoding.
"""


def append_write(filename="", text=""):
    """Append text content to the end of a file.

    This function opens a file in append mode and adds the provided text
    to the end of the file. If the file doesn't exist, it will be created.
    The operation uses UTF-8 encoding for proper character handling.

    Args:
        filename (str): The path to the file where text will be appended.
                       Defaults to empty string.
        text (str): The text content to append to the file.
                   Defaults to empty string.

    Returns:
        int: The number of characters appended to the file.

    Raises:
        IOError: If there are issues writing to the file.
        PermissionError: If there are insufficient permissions to write
                        the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
