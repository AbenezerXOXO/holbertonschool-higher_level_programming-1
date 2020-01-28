#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class testclass(unittest.TestCase):
    """
    This class contains unittests for Rectangle class
    """
    def test_instantiation(self):
        """
        method that holds the tests related to __init__ method
        """
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(5, 5, 5, 5, None)
        self.assertNotEqual(r2.id, None)

    def test_private_attributes(self):
        """ checks if attributes are private """
        r1 = Rectangle(5, 5)
        with self.assertRaises(AttributeError):
            print(r1.__width)
        with self.assertRaises(AttributeError):
            print(r1.__height)
        with self.assertRaises(AttributeError):
            print(r1.__x)
        with self.assertRaises(AttributeError):
            print(r1.__y)

    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            r3 = Rectangle()
        with self.assertRaises(TypeError):
            r3 = Rectangle(1)

    def test_validation(self):
        """
        method to test validation of width, height, x and y
        """
        with self.assertRaises(TypeError):
            r3 = Rectangle("h", "j")
        with self.assertRaises(TypeError):
            r3 = Rectangle(5, "j")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "a", 8)
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, 3, "j")
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, 5, -1, 7)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, 5, 7, -2)

    def test_area(self):
        """ test area method """
        r3 = Rectangle(5, 5)
        self.assertEqual(r3.area(), 25)
