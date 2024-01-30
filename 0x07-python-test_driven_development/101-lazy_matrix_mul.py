#!/usr/bin/ppython3
"""
matrix multiplication using Numpy

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies two matrixes and returns new matrix
    representing the prodct

    args:
    m_a: first matrix
    m_b: second matrix
    """
    return np.matmul(m_a, m_b)
