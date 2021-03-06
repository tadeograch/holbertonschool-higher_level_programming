#!/usr/bin/python3
'''
Rectangle class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Inherits from BaseGeometry class'''
    def __init__(self, width, height):
        '''Intsantation and validation of width an height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
