#!/usr/bin/python3
"""Module defining a Student class for student information management.

This module provides a Student class that represents a student with basic
information like first name, last name, and age, with functionality to
convert the student instance to a JSON-compatible dictionary.
"""


class Student:
    """Represent a student with personal information.

    This class encapsulates student data including first name, last name,
    and age, providing methods to work with this data in JSON format.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance."""
        if isinstance(attrs, list):
            new_dict = dict()
            for atr in attrs:
                if hasattr(self, atr):
                    new_dict[atr] = self.__dict__[atr]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
