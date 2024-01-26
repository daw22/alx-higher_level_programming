#!/usr/bin/python3
# 2-matrix_divided.py by Dawit Yifru
"""
module containing a matrix divider

"""


def matrix_divided(matrix, div):
    """
    divides a matrix with div and returns
    a new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    r_size = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != r_size:
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for j in range(len(matrix[0])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    result = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(r_size):
            tmp.append(round(matrix[i][j] / div, 2))
        result.append(tmp)

    return result
