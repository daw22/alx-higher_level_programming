#!/usr/bin/python3
"""
calss the inherits from list

"""


class MyList(list):
    """
    inherits from list and add fuctionality
    """
    def print_sorted(self):
        """
        prints list items in ascending order
        """
        print(sorted(self))
