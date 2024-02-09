#!/usr/bin/python3
import unittest
from models.base import Base

"""
Unit test for the base module
"""


class test_base(unittest.TestCase):
    """
    Test cases
    """
    def test_base_no_arg(self):
        """
        testing Base init with no arg
        """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_base_int(self):
        """
        testing Base init with int arg
        """
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_base_0_arg(self):
        """
        testing Base init with '0' arg
        """
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_base_negative_int(self):
        """
        testing Base init with negative int
        """
        base = Base(-2)
        self.assertEqual(base.id, -2)

    def test_base_float(self):
        """
        testing Base init with float
        """
        base = Base(1.1)
        self.assertEqual(base.id, 1.1)

    def test_base_string(self):
        """
        testing Base init with string
        """
        base = Base("Hello")
        self.assertEqual(base.id, "Hello")
    
    def test_base_list(self):
        """
        testing Base init with list arg
        """
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_base_dict(self):
        """
        testing Base init with dict arg
        """
        base = Base({"one": 1, "two": 2})
        self.assertEqual(base.id, {"one": 1, "two": 2})

    def test_base_tuple(self):
        """
        testing Base init with tupel arg
        """
        base = Base((1, 2, 3))
        self.assertEqual(base.id, (1, 2, 3))

