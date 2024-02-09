#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""
test_rectangle.py
"""


class test_rectangle(unittest.TestCase):
    """
    Test cases for rectangle class
    """
    def setUp(self):
        """
        setting up a rectangle instance for testing
        """
        self.rec = Rectangle(10, 20)

    def tearDown(self):
        """"
        remove Rectangle instance after test
        """
        del self.rec

    # test the getters
    def test_width_getter(self):
        """
        tests width getter
        """
        self.assertEqual(self.rec.width, 10)

    def test_height_getter(self):
        """
        tests height getter
        """
        self.assertEqual(self.rec.height, 20)

    def test_x_getter(self):
        """
        tests x getter
        """
        self.assertEqual(self.rec.x, 0)

    def test_y_getter(self):
        """
        tests y getter
        """
        self.assertEqual(self.rec.y, 0)

    # test the setters
    def test_width_setter(self):
        """
        tests width setter
        """
        self.rec.width = 5
        self.assertEqual(self.rec.width, 5)
        with self.assertRaises(TypeError):
            rec = Rectangle("a", 20)
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 20)

    def test_height_setter(self):
        """
        tests height setter
        """
        self.rec.height = 10
        self.assertEqual(self.rec.height, 10)
        with self.assertRaises(TypeError):
            rec = Rectangle(10, "q")
        with self.assertRaises(ValueError):
            rec = Rectangle(10, -1)

    def test_x_setter(self):
        """
        tests x setter
        """
        self.rec.x = 100
        self.assertEqual(self.rec.x, 100)
        with self.assertRaises(TypeError):
            rec = Rectangle(10, 20, "q")
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 20, -1)

    def rest_y_setter(self):
        """
        tests y setter
        """
        self.rec.y = 100
        self.assertEqual(self.rec.y, 100)
        with self.assertRaises(TypeError):
            rec = Rectangle(10, 20, 1, "q")
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 20, 1, -1)

    # test for missing args
    def test_missing_w_h(self):
        """
        test with missing width and height
        """
        with self.assertRaises(TypeError):
            rec = Rectangle()
        with self.assertRaises(TypeError):
            rec = Rectangle(1)
