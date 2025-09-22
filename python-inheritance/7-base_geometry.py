#!/usr/bin/python3


class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods"""

    def area(self):
        """Raises an Exception with message area() is not implemented"""
        pass

    def integer_validator(self, name, value):
        """Validates value"""
        pass
