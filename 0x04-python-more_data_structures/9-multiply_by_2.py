#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    keys = list(a_dictionary)
    new_dict = {}
    for key in keys:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
