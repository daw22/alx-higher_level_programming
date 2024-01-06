#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for j in arr:
            if j != arr[-1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print("")
