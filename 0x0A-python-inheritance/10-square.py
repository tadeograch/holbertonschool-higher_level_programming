#!/usr/bin/python3
'''Square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Inherits from rectangle'''
    def __init__(self, size):
        '''Intsantation and validation of size'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Method that returns the area'''
        return self.__size ** 2

    def __str__(self):
        '''Return string'''
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
