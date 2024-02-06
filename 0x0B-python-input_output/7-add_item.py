#!/usr/bin/python3
"""
contains a function that loads a python list
from a file and add arguments to it, and save the
new list to a file
"""
import sys


if __name__ == "__main__":
    save_t_f = __import__("5-save_to_json_file").save_to_json_file
    load_f_f = __import__("6-load_from_json_file").load_from_json_file
    try:
        _list = load_f_f("add_item.json")
    except FileNotFoundError:
        _list = []
    _list.extend(sys.argv[1:])
    save_t_f(_list, "add_item.json")
