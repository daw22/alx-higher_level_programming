#!/usr/bin/python3
"""
contains a strudent class defination
"""


class Student:
    """
    A student class
    """
    def __init__(self, first_name, last_name, age):
        """
        intialazes a student instance
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary representation of a student
        object
        """
        return self.__dict__
