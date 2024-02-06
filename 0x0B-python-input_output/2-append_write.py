#!/usr/bin/python3
"""
contains a function tha appends to a file
"""


def append_write(filename="", text=""):
    """
    Appends text to a file that exist or creates a new file
    if it doesn't exist
    Args:
        filename: the file to append/write to
        text: the text to append/write to the file
    """
    with open(filename, "a", encoding='utf8') as f:
        return f.write(text)
