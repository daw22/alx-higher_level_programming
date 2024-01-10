#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_string = roman_string.upper()
    roman_numeral_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    prev = 0
    result = 0
    for r in roman_string:
        value = roman_numeral_map[r]
        if value is None:
            return None
        if value > prev:
            result += value - (2 * prev)
        else:
            result += value
        prev = value
    return result
