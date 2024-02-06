#!/usr/bin/python3
"""
contains a function that deserialazes a json string
"""
import json


def from_json_string(my_str):
    """
    Deserializes a json string and returns it
    Args:
        my_str: json string to be deserialized
    """
    return json.loads(my_str)
