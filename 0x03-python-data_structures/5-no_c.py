#!/usr/bin/python3

def no_c(my_string):
    my_str = list(my_string)
    cs = my_str.count("c")
    Cs = my_str.count("C")
    for i in range(cs):
        my_str.remove("c")
    for j in range(Cs):
        my_str.remove("C")
    return "".join(my_str)
