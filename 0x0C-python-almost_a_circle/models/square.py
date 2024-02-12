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
        self.size = size
        self.y = y
        self.x = x
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overides default __str__
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        getter for size
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of class square
        """
        if args is not None and len(args) != 0:
            if not isinstance(args[0], int) and arg[0] is not None:
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        returns a dictionary representation of
        a square instance
        """
        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}
