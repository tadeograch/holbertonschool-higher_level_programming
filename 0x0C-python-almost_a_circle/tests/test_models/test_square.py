#!/usr/bin/python3
'''Unittest for Rectangle'''
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Testing Square class'''
    def test_cases(self):
         '''Testing simple cases'''
         Base._Base__nb_objects = 0
         self.assertEqual(Square(10, 2).id, 1)
         self.assertEqual(Square(10, 2).size, 10)
         self.assertEqual(Square(10, 2, 5, 3).id, 3)

    def test_mandatory_size(self):
        '''Test that size is a mandatory arg'''
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_typeerror(self):
        '''Test size TypeError'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("Holberton", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(True , 1)

    def test_size_valueerror(self):
        '''Test size TypeError'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(-3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0, 1)

    def test_x_typeerror(self):
        '''Test x TypeError'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, "Holberton")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, True)
    
    def test_x_valueerror(self):
        '''Test x ValueError'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(1,-3)

    def test_y_typeerror(self):
        '''Test y TypeError'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 2, "Holberton")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 2, True)

    def test_y_valueerror(self):
        '''Test y ValueError'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(1, 2, -4)

    def test_rectangle_area(self):
        '''Test area'''
        Base._Base__nb_objects = 0
        r = Square(2)
        self.assertEqual(r.area(), 4)
        r  = Square(3, 4, 5, 6)
        self.assertEqual(r.area(), 9)

    def test_display(self):
        '''Test display'''
        Base._Base__nb_objects = 0
        
        r = Square(3)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), ("###\n###\n###\n"))

        r = Square(3, 3)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), ("   ###\n   ###\n   ###\n"))

        r = Square(3, 3, 3)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), ("\n\n\n   ###\n   ###\n   ###\n"))

    def test_str(self):
        '''Test str method'''
        Base._Base__nb_objects = 0
        
        r = Square(2)
        r_str = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(r), r_str)

        r = Square(2, 3, 4)
        r_str = "[Square] (2) 3/4 - 2"
        self.assertEqual(str(r), r_str)

        r = Square(2, 3, 4, 5)
        r_str = "[Square] (5) 3/4 - 2"
        self.assertEqual(str(r), r_str)

    def test_update(self):
        '''Test update'''
        Base._Base__nb_objects = 0

        r = Square(2)
        r_str = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(r), r_str)

        r.update(89)
        r_str = "[Square] (89) 0/0 - 2"
        self.assertEqual(str(r), r_str)

        r.update(89, 3)
        r_str = "[Square] (89) 0/0 - 3"
        self.assertEqual(str(r), r_str)

        r.update(89, 3, 4, 5)
        r_str = "[Square] (89) 4/5 - 3"
        self.assertEqual(str(r), r_str)

    def test_update_args_setter(self):
        '''tests that the update method uses setter with *args'''
        r = Square(1, 1, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, -1)

    def test_update_too_many_args(self):
        '''test too many args for update'''
        r = Square(1, 1, 0, 1)
        r.update(1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Square] (1) 1/1 - 1")

    def test_update_no_args(self):
        '''test no args for update'''
        Base._Base__nb_objects = 0
        r = Square(1, 1, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Square] (1) 1/0 - 1")

    def test_update_kwargs(self):
        '''Testing the update method with **kwargs'''
        r = Square(1, 0, 0, 1)
        self.assertEqual(str(r), "[Square] (1) 0/0 - 1")
        r.update(size=11, x=2)
        self.assertEqual(str(r), "[Square] (1) 2/0 - 11")
        r.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(r), "[Square] (89) 5/3 - 4")
        r.update(x=6, y=8, size=9)
        self.assertEqual(str(r), "[Square] (89) 6/8 - 9")

    def test_update_kwargs_setter(self):
        '''tests that the update method uses setter with **kwargs'''
        r = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(size="hello")
        with self.assertRaises(TypeError):
            r.update(x="hello")
        with self.assertRaises(TypeError):
            r.update(y="hello")
        with self.assertRaises(ValueError):
            r.update(size=-1)
        with self.assertRaises(ValueError):
            r.update(size=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_mix_args_kwargs(self):
        '''tests output for mixed args and kwargs'''
        r = Square(1, 0, 0, 1)
        r.update(2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Square] (2) 2/2 - 2")

    def test_extra_kwargs(self):
        '''tests for random kwargs'''
        r = Square(1, 0, 0, 1)
        r.update(hello=2)
        self.assertEqual(str(r), "[Square] (1) 0/0 - 1")

    def test_to_dict(self):
        '''test regular to_dictionary'''
        Base._Base__nb_objects = 0

        r = Square(2, 3, 4, 5)
        d1 = r.to_dictionary()
        self.assertEqual({"id": 5, "size": 2, "x": 3, "y": 4},
                         d1)
        r = Square(3, 4, 0)
        d2 = r.to_dictionary()
        self.assertEqual({"id": 1, "size": 3, "x": 4, "y": 0},
                         d2)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)

        r = Rectangle(1, 1, 1, 1, 1)

if __name__ == '__main__':
    unittest.main()