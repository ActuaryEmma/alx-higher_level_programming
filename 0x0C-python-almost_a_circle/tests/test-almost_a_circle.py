"""
unittest module and models,base module  are imported
models.base allo access and test the functionality of a base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """defines a test case class"""

    def setUp(self):
        """
        called before each test method runs.
        reset __nb_objects of the Base class to 0
        """
        Base._Base__nb_objects = 0

    def test_nb_object_initial_value(self):
        """check if the initial value of _nb_object is zero"""
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_nb_objects_increment(self):
        """
        create two instances
        checks if __nb_objects is correctly incremented to 2
        after creating the instances
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_nb_objects_private_access(self):
        """check if __nb_objects is a priviate class attribute"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_constructor_with_id(self):
        """check if id attribute of an instance of Base is correctly set"""
        base3 = Base(4)
        self.assertEqual(base3.id, 4)

    def test_constructor_without_id(self):
        """
        check if id is not passed the new value of __nb_objects is passed to id
        """
        base4 = Base()
        base5 = Base()
        self.assertEqual(base4.id, 1)
        self.assertEqual(base5.id, 2)


if __name__ == '__main__':
    unittest.main()
