#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
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
        testing Base init with tuple arg
        """
        base = Base((1, 2, 3))
        self.assertEqual(base.id, (1, 2, 3))

    def test_to_json_none(self):
        """
        tests to_json_string with none
        """
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_type(self):
        """
        tests return type of to_json_string func
        """
        sqr = Square(5)
        sqr_dict = sqr.to_dictionary()
        sqr_json = Base.to_json_string([sqr_dict])
        self.assertEqual(type(sqr_json), str)

    def test_to_json_ret(self):
        """
        tests return value of to_json_string func
        """
        rec = Rectangle(10, 20, 2, 4, 444)
        rec_dict = rec.to_dictionary()
        rec_json = Base.to_json_string([rec_dict])
        self.assertEqual(json.loads(rec_json),
                         [{"id": 444, "y": 4, "x": 2, "width": 10,
                           "height": 20}])
