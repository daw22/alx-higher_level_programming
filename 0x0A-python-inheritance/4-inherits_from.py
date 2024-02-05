#!/usr/bin/python3
"""
contains function that checks if an object inherits
from a class directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    checks if obj inherits from a_class
    directly or indirectly
    """
    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False
