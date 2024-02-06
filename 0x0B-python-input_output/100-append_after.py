#!/usr/bin/python3
"""
100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new_string after each line containing
    the search_string
    Args:
        filename: the file to append text to
        search_string: a string to look for in the file
        new_strng: the string to append
    """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w") as f:
        f.writelines(lines)
