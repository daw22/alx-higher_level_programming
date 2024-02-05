#!/usr/bin/python3
"""
class the inherits from list

"""


class MyList(list):
    """
    inherits from list and adds a method
    """
    def print_sorted(self):
        """
        prints list items in ascending order
        """
        print(sorted(self))
