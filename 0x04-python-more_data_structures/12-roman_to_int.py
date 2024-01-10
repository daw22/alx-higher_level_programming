#!/usr/bin/python3

def roman_to_int(roman_string):
    r_str = roman_string.upper()
    r_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    init_val = 0
    for i in range(len(r_str)):
        if i > 0 and r_map[r_str[i]] > r_map[r_str[i - 1]]:
            init_val += r_map[r_str[i]] - 2 * r_map[r_str[i - 1]]
        else:
            init_val += r_map[r_str[i]]
    return init_val
