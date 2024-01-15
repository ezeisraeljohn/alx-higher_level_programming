import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):

    def setUp(self) -> None:
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base()

    def test_num_of_obj(self):
        self.assertEqual(self.base3.id, self.base2.id + 1)

    def test_num_of_obj2(self):
        self.assertEqual(self.base3.id, self.base1.id + 2)

    def test_accessing_nb_objects(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects
 
    def test_passing_unrequired_arg(self):
        with self.assertRaises(TypeError):
            Base(3, 2)
