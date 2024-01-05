#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for j in arr:
            print("{:d}".format(j), end="")
        print("")
