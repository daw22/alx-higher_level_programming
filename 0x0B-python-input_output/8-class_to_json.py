#!/usr/bin/python3
"""
contains a function that change a python class to
a json string
"""


def class_to_json(obj):
    """
    returns a dictionary representation of a python class
    """
    return obj.__dict__
