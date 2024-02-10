#!/usr/bin/python3
from models.base import Base
"""
rectangle.py
"""


class Rectangle(Base):
    """
    Rectangle class that extends the base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intializes a Rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: poistion of the rectangle on x co-ordinate
            y: position of the rectangle on y co-ordinate
            id: id of the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculate and returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the 'Rectangle' instance with
        the character '#'
        """
        for v in range(self.y):
            print("")
        for h in range(self.height):
            for hr in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        overides default __str__
        """
        return "[Rectangle]" + " (" + str(self.id) + ") " + str(self.x) \
            + "/" + str(self.y) + " - " + str(self.width) + "/" \
            + str(self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        *args(present):
            1st arg should be - id
            2nd arg should be - width
            3rd arg should be - height
            4th arg should be - x
            5th arg should be - y
        **kwargs(args not present): key/value pair of attributes
                                  of any order
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
