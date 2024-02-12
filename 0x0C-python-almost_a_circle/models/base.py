#!/usr/bin/python3
import json
from pathlib import Path
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
        if (not isinstance(list_dictionaries, list) or
                not all(isinstance(d, dict) for d in list_dictionaries)):
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
                dict_l = [lst.to_dictionary() for lst in list_objs]
                jfile.write(Base.to_json_string(dict_l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns a list of dict from json string
        """
        dict_list = []
        if json_string is not None and json_string != "":
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")
            dict_list = json.loads(json_string)
        return dict_list

    @classmethod
    def create(cls, **dictionary):
        """
        creates an intance with all attrs set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 20)
        if cls.__name__ == "Square":
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loads instances from a file
        """
        f_name = cls.__name__ + ".json"
        dict_list = []
        inst_list = []
        if Path(f_name).is_file():
            with open(f_name, "r") as j_file:
                text = j_file.read()
            dict_list = cls.from_json_string(text)
            for dictn in dict_list:
                inst_list.append(cls.create(**dictn))

        return inst_list
