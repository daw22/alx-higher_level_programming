#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    divider = 0
    if not my_list:
        return 0
    for i in my_list:
        total += i[0] * i[1]
        divider += i[1]
    return total / divider
