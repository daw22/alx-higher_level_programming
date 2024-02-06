#!/usr/bin/python3
"""
contains a function that writes an object to
file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes and saves an object to a file
    Args:
        my_obj: the object to save
        filename: the file to write to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
