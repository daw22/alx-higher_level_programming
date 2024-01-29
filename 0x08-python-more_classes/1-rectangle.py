#!/usr/bin/python3
"""
A simple rectangle class

"""


class Rectangle:
    """
    A simple rectangle class with optional width
    and height intialization and getter and setter
    methods
    """
    def __init__(self, width=0, height=0):
        """
        Intializes a rectancle instance
        Args:
           width: width of the rectange
           height: height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
