#!/usr/bin/python3
# 102-square.py by Dawit Yifru
"""Defines a square class"""


class Square:
    """Defines square calss tha have methods to
        calculate area and compare squares based
        on their areas"""
    def __init__(self, size=0):
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()
