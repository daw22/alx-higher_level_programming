#!/usr/bin/python3
"""
contains a function that reads from a file
"""


def read_file(filename=""):
    """
    Reads from a text file and prints it
    out to stdout
    Args:
        filename: the file to read from
    """
    with open(filename, encoding="utf8") as f:
        data = f.read()

    print(data, end='')
