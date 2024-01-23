#!/usr/bin/python3
# 3-square.py by Dawit yifru
"""Define square class"""


class Square:
    """Define a class for a square with an
        area method"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
