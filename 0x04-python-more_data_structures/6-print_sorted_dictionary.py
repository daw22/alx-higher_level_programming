#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary))
    new_dict = {}
    for key in keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
