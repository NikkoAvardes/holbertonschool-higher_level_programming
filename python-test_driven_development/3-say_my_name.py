#!/usr/bin/python3
"""
This module contains a function that prints a person's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person's full name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
        Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Jane")
        My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name} ")
