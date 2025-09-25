#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def area(self):
        """Calculate shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate shape perimeter."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Display shape info using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
