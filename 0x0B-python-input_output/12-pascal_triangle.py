#!/usr/bin/python3
"""
contains implementation of a pascal triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of n lists that represent
    pascal's triangle
    Args:
        n: height of triangle
    """
    if n < 0:
        return []
    lists = [[1]]
    while n != len(lists):
        lst = lists[-1]
        tmp = [1]
        for i in range(len(lst) - 1):
            tmp.append(lst[i] + lst[i + 1])
        tmp.append(1)
        lists.append(tmp)
    return lists
