#!/usr/bin/python3
"""
contains a function that loads a python
object from a file
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a file
    Args:
        filename: the file to read from
    """
    with open(filename, "r") as f:
        return json.load(f)
