#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        """Test the function with diferent cases"""
        self.assertEqual(max_integer([1, 5, -7, 6, -4 , 10]), 10)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 3 + 2, 7, 9 * 8, 35, 12]), 72)

    def test_empty_list(self):
        """Test the function with empty list"""
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_exceptions(self):
        """Test the exceptions"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [1, 4, "H", 12, None, [2, 5], 12.9])

    if __name__ == '__main__':
        unittest.main()
