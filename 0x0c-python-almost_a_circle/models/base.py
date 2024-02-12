#!/usr/bin/python3
import json
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json representaion of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(d) == dict for d in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save json string rep of list_objcts to a file
        """
        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                l_dict = [l.to_dictionary() for l in list_objs]
                jfile.write(Base.to_json_string(l_dict))
