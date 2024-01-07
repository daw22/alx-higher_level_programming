#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return []
    arr = []
    for n in my_list:
        if n % 2 == 0:
            arr.append(True)
        else:
            arr.append(False)
    return arr
