#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_values(self):
        """Test for numbers output"""
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([1, 2, 4, 3]), 4)

    def test_type_error(self):
        """Test for type error """
        self.assertRaises(TypeError, max_integer("12"))
