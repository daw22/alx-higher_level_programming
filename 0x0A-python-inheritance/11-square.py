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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        overides str() method
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
