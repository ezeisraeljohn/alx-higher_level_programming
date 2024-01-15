import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_same_value(self):
        self.assertEqual(Base().id, 2)

    def test_empty_parameter(self):
        self.assertEqual(Base().id, 1)