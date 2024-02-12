#!/usr/bin/python3
import unittest
from models.square import Square
from io import StringIO
import sys
import json
"""
test_square.py
"""


class test_rectangle(unittest.TestCase):
    """
    Test cases for square class
    """
    def setUp(self):
        """
        setting up a Square instance for testing
        """
        self.sqr = Square(10)

    def tearDown(self):
        """"
        remove Square instance after test
        """
        del self.sqr

    # test the getters
    def test_width_getter(self):
        """
        tests width getter
        """
        self.assertEqual(self.sqr.width, 10)

    def test_height_getter(self):
        """
        tests height getter
        """
        self.assertEqual(self.sqr.height, 10)

    def test_x_getter(self):
        """
        tests x getter
        """
        self.sqr.x = 5
        self.assertEqual(self.sqr.x, 5)

    def test_y_getter(self):
        """
        tests y getter
        """
        self.sqr.y = 5
        self.assertEqual(self.sqr.y, 5)

    # test the setters
    def test_size_setter(self):
        """
        tests size setter
        """
        self.sqr.width = 5
        self.assertEqual(self.sqr.width, 5)
        with self.assertRaises(TypeError):
            sqr = Square("a")
        with self.assertRaises(ValueError):
            sqr = Square(0)

    def test_x_setter(self):
        """
        tests x setter
        """
        self.sqr.x = 100
        self.assertEqual(self.sqr.x, 100)
        with self.assertRaises(TypeError):
            sqr = Square(10, "q")
        with self.assertRaises(ValueError):
            sqr = Square(10, -1)

    def test_y_setter(self):
        """
        tests y setter
        """
        self.sqr.y = 100
        self.assertEqual(self.sqr.y, 100)
        with self.assertRaises(TypeError):
            sqr = Square(10, 1, "q")
        with self.assertRaises(ValueError):
            sqr = Square(10, 1, -1)

    # test for missing args
    def test_missing_w_h(self):
        """
        test with missing width and height
        """
        with self.assertRaises(TypeError):
            sqr = Square()
        with self.assertRaises(TypeError):
            sqr = Square(10, 5, 5, 111, 1)

    # test area func
    def test_area(self):
        """
        test the area function
        """
        self.assertEqual(self.sqr.area(), 100)

    # test display_rec
    def test_display(self):
        """
        tests display(without x and y)
        """
        strio = StringIO()
        sys.stdout = strio
        sqr = Square(2)
        sqr.display()
        sys.stdout = sys.__stdout__
        result = "##\n##\n"
        self.assertEqual(result, strio.getvalue())

    def test_display_x_y(self):
        """
        test display(wiht x and y)
        """
        strio = StringIO()
        sys.stdout = strio
        sqr = Square(3, 2, 2)
        sqr.display()
        sys.stdout = sys.__stdout__
        result = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(result, strio.getvalue())

    # test __str__() overite
    def tesr_str(self):
        """
        tests __str__() output
        """
        sqr = Square(10, 5, 10, 120)
        self.assertEqual(sqr.__str__(), "[Square] (120) 5/10 - 10")

    # test update method
    def test_update_args(self):
        """
        test update method
        """
        sqr = Square(10, 2, 3, 100)

        sqr.update(300)
        self.assertEqual(sqr.id, 300)

        sqr.update(300, 30)
        self.assertEqual(sqr.size, 30)

        sqr.update(300, 50, 10)
        self.assertEqual(sqr.x, 10)

        sqr.update(300, 30, 10, 20)
        self.assertEqual(sqr.y, 20)

    def test_update_kwargs(self):
        """
        tests modified update method with **kwargs
        """
        sqr = Square(10, 2, 3, 100)
        sqr.update(200, 25, 5, 6)
        self.assertEqual(sqr.id, 200)
        self.assertEqual(sqr.size, 25)
        self.assertEqual(sqr.x, 5)
        self.assertEqual(sqr.y, 6)

        sqr.update(id=111)
        self.assertEqual(sqr.id, 111)

        sqr.update(size=50)
        self.assertEqual(sqr.size, 50)

        sqr.update(x=9)
        self.assertEqual(sqr.x, 9)

        sqr.update(y=11)
        self.assertEqual(sqr.y, 11)

        sqr.update(333, y=22)
        self.assertEqual(sqr.id, 333)
        self.assertEqual(sqr.y, 11)

    def test_to_dictionary(self):
        """
        tests to_dict func return type
        """
        sqr = Square(10)
        self.assertEqual(type(sqr.to_dictionary()), dict)

    def test_to_dictionary_ret(self):
        """
        tests the output of to_dictionary func
        """
        sqr = Square(5, 0, 2, 111)
        sqr_dict = sqr.to_dictionary()

        self.assertEqual(sqr_dict, {"id": 111, "size": 5, "x": 0, "y": 2})

    def test_save_to_file(self):
        """
        tests save_to_file parent class function
        """
        sqr = Square(10, 5, 2, 777)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as sqr_f:
            text = sqr_f.read()
        exp = [{"id": 777, "size": 10, "x": 5, "y": 2}]
        self.assertEqual(exp, json.loads(text))

    def test_save_to_file_none(self):
        """
        tests save_to_file func with None
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as sqr_f:
            text = sqr_f.read()
        self.assertEqual(text, "[]")

    def test_save_file_none_list(self):
        """
        test save_to_file with non list
        """
        with self.assertRaises(TypeError):
            Square.save_to_file(self.sqr)

    def test_from_json_string(self):
        """
        test from json_string
        """
        sqr1 = Square(10, 2, 2, 101)
        sqr2 = Square(5, 1, 1, 202)
        sqr_dict1 = sqr1.to_dictionary()
        sqr_dict2 = sqr2.to_dictionary()
        sqr_str = Square.to_json_string([sqr_dict1, sqr_dict2])
        sqr_dict_list = Square.from_json_string(sqr_str)

        self.assertEqual(type(sqr_dict_list), list)
        self.assertEqual(sqr_dict_list, [sqr_dict1, sqr_dict2])
        self.assertEqual(sqr_dict_list[0], sqr_dict1)
        self.assertEqual(sqr_dict_list[1], sqr_dict2)

    def test_creat_from_dict(self):
        """
        tests create
        """
        sqr = Square(10)
        sqr_dict = sqr.to_dictionary()
        sqr1 = Square.create(**sqr_dict)

        self.assertIsNot(sqr, sqr1)
        self.assertNotEqual(sqr, sqr1)
        self.assertEqual(sqr.size, sqr1.size)
