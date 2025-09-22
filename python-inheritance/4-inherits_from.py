#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Returns True if obj inherited (directly or indirectly) from a_class"""
    return issubclass(type(obj), a_class)
