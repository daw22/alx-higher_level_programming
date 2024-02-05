#!/usr/bin/python3
"""
contains a function that checks if args are
of the same class

"""


def is_same_class(obj, a_class):
    """
    chaecks if obj is instance of a_class
    """
    return type(obj) == a_class
