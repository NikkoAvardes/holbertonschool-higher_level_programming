#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract animal class."""

    @abstractmethod
    def sound(self):
        """Return animal sound."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        return ("Bark")


class Cat(Animal):
    """Cat class."""

    def sound(self):
        return ("Meow")
