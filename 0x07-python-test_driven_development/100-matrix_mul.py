#!/usr/bin/python3
# 100-matrix_mul.py by Daiwt Yifru
"""
Matrix multiplication

"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrixes
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for k in m_a:
        if not isinstance(k, list):
            raise TypeError("m_a must be a list of lists")
    for m in m_b:
        if not isinstance(m, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # now multiply the matrixes
    r_m = []
    for i in range(len(m_b[0])):
        row = []
        for j in range(len(m_b)):
            row.append(m_b[j][i])
        r_m.append(row)

    c_m = []
    for r in m_a:
        row = []
        for c in r_m:
            total = 0
            for m in range(len(r_m[0])):
                total += r[m] * c[m]
            row.append(total)
        c_m.append(row)

    return c_m
