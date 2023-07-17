"""
unittests - helps run the tests
Base and Rectangle has the function to test
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class with Rectangle class testcases"""
    def setUp(self):
        """executed before each test"""
        Base.__Base__nb_objects = 0

    def test_constructor_width_height(self):
        """return value of id, width and height when we have a valid inputs"""
        rec1 = Rectangle(10, 2)
        rec2 = Rectangle(2, 10)
        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec1.width, 10)
        self.assertEqual(rec1.height, 2)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec2.id, 2)
        self.assertEqual(rec2.width, 2)
        self.assertEqual(rec2.height, 10)
        self.assertEqual(rec2.x, 0)
        self.assertEqual(rec2.y, 0)

    def test_constructor_width_height_x_y(self):
        """return values width, height, x, y ,id when we have valid values"""
        rec3 = Rectangle(10, 2, 1, 2, 12)
        self.assertEqual(rec3.id, 12)
        self.assertEqual(rec3.width, 10)
        self.assertEqual(rec3.height, 2)
        self.assertEqual(rec3.x, 1)
        self.assertEqual(rec3.y, 2)

    def test_width_getter_setter(self):
        """return the correct values from getter and setter method"""
        rec4 = Rectangle(3, 6)
        rec4.width = 5
        self.assertEqual(rec4.width, 5)

    def test_height_getter_setter(self):
        """return the correct values from getter and setter method"""
        rec5 = Rectangle(3, 6)
        rec5.height = 10
        self.assertEqual(rec5.height, 10)

    def test_x_getter_setter(self):
        """return the correct values from getter and setter method"""
        rec6 = Rectangle(4, 5, 6, 1)
        rec6.x = 10
        self.assertEqual(rec6.x, 10)

    def test_y_getter_setter(self):
        """return the correct values from getter and setter method"""
        rec7 = Rectangle(4, 6, 10, 2)
        rec7.y = 4
        self.assertEqual(rec7.y, 4)

    def test_invalid_type(self):
        """return TypeError when we have invalid Width and height"""
        with self.assertRaises(TypeError) as e:
            rect = Rectangle(None, None)

    def test_invalid_type_width(self):
        """return TypeError when we have value of width as a string"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle("3", 6)

    def test_invalid_type0_width(self):
        """return TypeError when we have value of width is None"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle(None, 2)

    def test_invalid_type1_width(self):
        """return TypeError when we have value of width as a string"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle("type", 1)

    def test_invalid_type2_width(self):
        """return TypeError when we have value of width is a float"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle(6.6, 1)

    def test_invalid_type3_width(self):
        """return TypeError when we have value of width is a boolean"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle(False, 1)

    def test_invalid_type4_width(self):
        """return TypeError when we have value of width is a tuple"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle((1, 2), 1)

    def test_invalid_type5_width(self):
        """return TypeError when we have value of width is a set"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle({1, 2}, 1)

    def test_invalid_type6_width(self):
        """return TypeError when we have value of width is a complex value"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle(1j, 1)

    def test_invalid_type7_width(self):
        """return TypeError when we have value of width is a list"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle([1, 2, 3], 1)

    def test_invalid_type8_width(self):
        """return TypeError when we have value of width is a dictionary"""
        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle({"first": 1, "second": 2}, 1)

    def test_invalid_value_width(self):
        """return ValueError when we have value of width is a less than 1"""
        with self.assertRaises(ValueError) as e:
            rect8 = Rectangle(-1, 10)

    def test_invalid_type_height(self):
        """return TypeError when we have value of height is a string"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(3, "6")

    def test_invalid_type0_height(self):
        """return TypeError when we have value of height is None"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(2, None)

    def test_invalid_type1_height(self):
        """return TypeError when we have value of height is a string"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(5, "type")

    def test_invalid_type2_height(self):
        """return TypeError when we have value of height is a float"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(4, 6.6)

    def test_invalid_type3_height(self):
        """return TypeError when we have value of height is a boolean"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(5, False)

    def test_invalid_type4_height(self):
        """return TypeError when we have value of height is a tuple"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(5, (1, 2))

    def test_invalid_type5_height(self):
        """return TypeError when we have value of height is a set"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(4, {1, 2})

    def test_invalid_type6_height(self):
        """return TypeError when we have value of height is a complex value"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(5, 1j)

    def test_invalid_type7_height(self):
        """return TypeError when we have value of height is a list"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(5, [1, 2, 3])

    def test_invalid_type8_height(self):
        """return TypeError when we have value of height is a dictionary"""
        with self.assertRaises(TypeError) as e:
            rec9 = Rectangle(5, {"first": 1, "second": 2})

    def test_invalid_value_height(self):
        """return ValueError when we have value of height is a less than 1"""
        with self.assertRaises(ValueError) as e:
            rec9 = Rectangle(3, -1)

    def test_invalid_type_x(self):
        """return TypeError when we have value of x is a string"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, "6", 1)

    def test_invalid_type1_x(self):
        """return TypeError when we have value of x is a string"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, "type", 1)

    def test_invalid_type2_x(self):
        """return TypeError when we have value of x is a float"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, 6.6, 1)

    def test_invalid_type3_x(self):
        """return TypeError when we have value of x is a boolean"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, False, 1)

    def test_invalid_type4_x(self):
        """return TypeError when we have value of x is a tuple"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, (1, 2), 1)

    def test_invalid_type5_x(self):
        """return TypeError when we have value of x is a set"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, {1, 2}, 1)

    def test_invalid_type6_x(self):
        """return TypeError when we have value of x is a complex"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, 1j, 1)

    def test_invalid_type7_x(self):
        """return TypeError when we have value of x is a list"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, [1, 2, 3], 1)

    def test_invalid_type8_x(self):
        """return TypeError when we have value of x is a dictionary"""
        with self.assertRaises(TypeError) as e:
            rec10 = Rectangle(4, 5, {"first": 1, "second": 2}, 1)

    def test_invalid_value_x(self):
        """return ValueError when we have value of x is less than 0"""
        with self.assertRaises(ValueError) as e:
            rec10 = Rectangle(4, 5, -1, 1)

    def test_invalid_type_y(self):
        """return TypeError when we have value of y is a string"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 6, 10, "2")

    def test_invalid_type1_y(self):
        """return TypeError when we have value of y is a string"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, "type")

    def test_invalid_type2_y(self):
        """return TypeError when we have value of y is a float"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, 6.6)

    def test_invalid_type3_y(self):
        """return TypeError when we have value of y is a boolean"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, False)

    def test_invalid_type4_y(self):
        """return TypeError when we have value of y is a tuple"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, (1, 2))

    def test_invalid_type5_y(self):
        """return TypeError when we have value of y is a set"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, {1, 2})

    def test_invalid_type6_y(self):
        """return TypeError when we have value of y is a complex value"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, 1j)

    def test_invalid_type7_y(self):
        """return TypeError when we have value of y is a list"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 1, [1, 2, 3])

    def test_invalid_type8_y(self):
        """return TypeError when we have value of y is a dictionary"""
        with self.assertRaises(TypeError) as e:
            rec11 = Rectangle(4, 5, 2, {"first": 1, "second": 2})

    def test_invalid_value_y(self):
        """return ValueError when we have value of y is less than 0"""
        with self.assertRaises(ValueError) as e:
            rec11 = Rectangle(4, 6, 10, -1)


if __name__ == '__main__':
    unittest.main()
