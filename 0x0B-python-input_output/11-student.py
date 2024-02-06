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

    def to_json(self, attrs=None):
        """
        returns a dictionary representation of a student
        object if attrs is listof strings that
        represents ony thoes attributes included in
        the list
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
