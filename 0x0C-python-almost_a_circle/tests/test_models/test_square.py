#!/usr/bin/python3

"""Test the square module"""


import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ The test class for the Square method """

    def setUp(self):
        """ Setup method """
        self.square = Square(1, 1)

    def tearDown(self) -> None:
        """ Tear down method """
        pass

    def test_typeError_unrecognized_arg(self):
        """ test_typeError_unrecognized_arg method """
        with self.assertRaises(TypeError):
            Square(1, 3, 4, 3, 4, 5)

    def test_set_x_valueError(self):
        """ The test_set_x_valueError method"""
        with self.assertRaises(ValueError):
            self.square.x = -1

    def test_set_y_valueError(self):
        """ The test_set_y_valueError method"""
        with self.assertRaises(ValueError):
            self.square.y = -1

    def test_set_width_valueError(self):
        """ The test_set_width_valueError method"""
        with self.assertRaises(ValueError):
            self.square.width = 0

    def test_set_height_valueError(self):
        """ The test_set_height_valueError method """
        with self.assertRaises(ValueError):
            self.square.height = 0

    def test_typeError_width(self):
        """ The test_set_height_valueError method"""
        with self.assertRaises(TypeError):
            Square("1", 3)

    def test_TypeError_height(self):
        """ The test_TypeError_height method"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_TypeError_x(self):
        """ The test_TypeError_x method"""
        with self.assertRaises(TypeError):
            Square(1, 2, x="2")

    def test_TypeError_y(self):
        """ The test_TypeError_y method"""
        with self.assertRaises(TypeError):
            Square(1, 2, 4, y="3")
