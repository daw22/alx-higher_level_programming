#!/usr/bin/python3
"""
A rectangle class
"""


class Rectangle:
    """
    A simple rectangle class with optional width
    and height intialization and getter and setter
    methods
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Intializes a rectancle instance
        Args:
           width: width of the rectange
           height: height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Retutns area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """overites string representation of the rectangle"""
        rec = ""
        if self.width == 0 or self.height == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    rec += str(self.print_symbol)
                except Exception:
                    rec += type(self).print_symbol
            if i != self.height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        """overites default __repr__() to get a string repewsentation
        of a rectangle that can be used by eval()"""

        name = type(self).__name__
        return name + "(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """overites del() function to add deletion message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a1 = rect_1.area()
        a2 = rect_2.area()
        if a1 == a2 or a1 > a2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """creates a square"""
        return Rectangle(size, size)
