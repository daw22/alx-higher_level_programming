#!/usr/bin/python3
# 0-add_integer by dawit Yifru
"""
contanins add_integer function


"""


def add_integer(a, b=98):
    """
    adds two integers and returns the resut
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
