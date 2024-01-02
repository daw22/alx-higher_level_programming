#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    i = 0
    for j in range(0, len(str)):
        if i != n:
            new_str.append(str[j])
        i += 1
    return "".join(new_str)
