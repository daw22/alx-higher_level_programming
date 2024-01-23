#!/usr/bin/python3
"""Magic class"""
import math


class MagicClass:
    def __init__(self, radius):
        """
        Initializes the MagicClass object with the given radius.

        Args:
            radius (int or float): The radius of the object.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0  # Initialize radius to 0 as a placeholder

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Calculates the area of the MagicClass object.

        Returns:
            float: The area of the object.
        """
        return math.pi * self.__radius**2

    def circumference(self):
        """
        Calculates the circumference of the MagicClass object.

        Returns:
            float: The circumference of the object.
        """
        return 2 * math.pi * self.__radius
