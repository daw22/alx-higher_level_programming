#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    outer = []
    for i in matrix:
        inner = []
        for j in i:
            inner.append(j**2)
        outer.append(inner)
    return outer
