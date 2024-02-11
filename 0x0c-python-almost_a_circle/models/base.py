#!/usr/bin/python3
"""
base.py
"""


class Base():
    """
    This is a Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        A constrictor for Base class
        Args:
            id: id's an object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
