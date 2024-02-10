#!/usr/bin/python3
from models.rectangle import Rectangle
"""
square.py
"""


class Square(Rectangle):
    """
    A square class the represents a special
    type of rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Intializes a square instance
        Args:
            size: size of the square(width==height)
            x: horizontal position of the square
            y: vertical postion of the square
            id: id of the square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overides default __str__
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
