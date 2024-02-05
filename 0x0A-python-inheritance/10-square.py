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
        super().__init__(size, size)
        self.__size = size
