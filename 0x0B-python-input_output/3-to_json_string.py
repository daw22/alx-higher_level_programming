#!/usr/bin/python3
"""
contains a fuction that serializes an object
"""
import json


def to_json_string(my_obj):
    """
    Serializes an object to json string
    Args:
        my_obj: object to be serialized
    """
    return json.dumps(my_obj)
