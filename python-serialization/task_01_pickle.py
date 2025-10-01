#!/usr/bin/env python3
"""
Custom object serialization module using pickle.

This module provides a CustomObject class that can serialize and
deserialize itself using Python's pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class for demonstration of pickle serialization.

    This class represents a person with basic attributes and provides
    methods for serialization and deserialization using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.

        Prints the name, age, and student status to the console.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.

        Returns:
            None: Returns None on success or failure.
        """
        try:
            with open(filename, "wb") as f:
                return pickle.dump(self, f)
        except (Exception):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if failed.
        """
        try:
            with open(filename, 'rb') as e:
                deser = pickle.load(e)
                return deser
        except (Exception):
            return None
