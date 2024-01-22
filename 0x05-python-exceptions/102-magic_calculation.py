#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception("Too far")
            result += a ** i / b
    except Exception as e:
        print(e)
    result += b
    return result
