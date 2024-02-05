#!/usr/bin/python3
"""
contains a square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A square class based on Rectangle class
    """
    def __init__(self, size):
        """
        Creates a new square instance
        """
        self.validate_integer("size", size)
        self.__size = size

    def area(self):
        """
        calculate area of asquare
        """
        return self.__size * self.__size
