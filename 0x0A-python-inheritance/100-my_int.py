#!/usr/bin/python3
"""
Defines a class tha inherits from int
"""


class MyInt(int):
    """
    A class tha inherits from 'int'
    """
    def __eq__(self, other):
        """
        overides '__eq__' method from parent class
        """
        return self.real != other

    def __ne__(self, other):
        """
        overides '__ne__' method
        """
        return self.real == other
