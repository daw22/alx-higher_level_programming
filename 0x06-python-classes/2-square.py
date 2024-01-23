#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Constructs a sqare object by checking for proper
        size argument"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
