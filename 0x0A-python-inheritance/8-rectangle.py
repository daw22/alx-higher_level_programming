#!/usr/bin/python3
"""
contains a rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from
    BaseGeometry class
    """
    def __init__(self, width, height):
        """
        create a Rectangle instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
