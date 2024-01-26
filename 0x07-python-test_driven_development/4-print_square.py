#!/usr/bin/python3
# 4-print_square.py by Dawit Yifru
"""
contains a function that prints square

"""


def print_square(size):
    """
    prints a square of size size with #
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
