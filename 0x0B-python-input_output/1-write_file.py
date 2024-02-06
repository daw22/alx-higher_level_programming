#!/usr/bin/python3
"""
contains a function that writes to a file
"""


def write_file(filename="", text=""):
    """
    Writes to a file by overideing file's content
    if the file exists
    Args:
        filename: the file to write to
        text: the text to write to the file
    """
    with open(filename, "w", encoding="utf8") as f:
        return f.write(text)
