#!/usr/bin/python3
"""
contains a basic BaseGeometry class
"""


class BaseGeometry:
    """
    A basic gometry class with area and
    integer_validator public methods
    """
    def area(self):
        """
        calculates area of a geometic shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value to be a positive integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
