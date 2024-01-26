#!/usr/bin/python3
# 5-text_indentation.py by Dawit Yifru
"""
parsses and prints in put text

"""


def text_indentation(text):
    """
    This function prints texts by replacing ".", "?" and ":"
    with two new lines

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # strip spaces at the beginning of text if any
    cursor = 0
    while cursor < len(text) and text[cursor] == " ":
        cursor += 1

    while cursor < len(text):
        print(text[cursor], end="")
        if text[cursor] in ".?:" or text[cursor] == " ":
            if text[cursor] in ".?:":
                print("\n")
            cursor += 1
            while cursor < len(text) and text[cursor] == " ":
                cursor += 1
            continue
        cursor += 1
