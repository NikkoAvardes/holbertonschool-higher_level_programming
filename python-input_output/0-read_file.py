#!/usr/bin/python3
"""Module for reading and displaying file contents.

This module provides functionality to read text files and display their
contents to the standard output using UTF-8 encoding for proper character
handling.
"""


def read_file(filename=""):
    """Read and print the contents of a text file.

    This function opens a file with UTF-8 encoding, reads its entire contents,
    and prints the content to stdout. No return value is provided as the
    function directly outputs to the console.

    Args:
        filename (str): The path to the file to be read.
                       Defaults to empty string.

    Returns:
        None: This function prints directly to stdout and returns nothing.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there are issues reading the file.
    """
    with open(filename, encoding="utf-8") as e:
        read = e.read()
        print(read, end="")
