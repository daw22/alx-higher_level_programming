#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for function max_integer([..])"""

    def test_empty_list(self):
        """test with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """test with list with single int"""
        self.assertEqual(max_integer([2]), 2)

    def test_multiple_int_list(self):
        """test with list with multiple ints"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_with_negative(self):
        """test with negative and positive ints"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_float_and_int(self):
        """test with a mix of int and float"""
        self.assertEqual(max_integer([1.01, 1.1, -21.8, 0]), 1.1)

    def test_string(self):
        """test string"""
        str = "dawit"
        self.assertEqual(max_integer(str), 'w')

    def test_strings_list(self):
        """test with list of strings"""
        strs = ["dawit", "max", "pitch", "diamond"]
        self.assertEqual(max_integer(strs), "pitch")

    def test_empty_string(self):
        """test with empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
