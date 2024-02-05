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

    def area(self):
        """
        calculate area of a recrangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        overides str method
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
