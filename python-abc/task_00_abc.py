#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
Abstract Animal Class and its Subclasses
"""


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return ("Bark")


class Cat(Animal):
    def sound(self):
        return ("Meow")
