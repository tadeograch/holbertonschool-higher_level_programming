#!/usr/bin/python3
'''Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Instantation of attributes'''
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """converts to string"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                self.__x, self.__y, self.__width))

    @property
    def size(self):
        '''size getter'''
        return self.__width

    @size.setter
    def size(self, value):
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        '''assigns attributes'''
        my_attr = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, my_attr[i], args[i])
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square'''
        r_dict = {}
        r_dict['id'] = self.id
        r_dict['size'] = self.__width
        r_dict['x'] = self.__x
        r_dict['y'] = self.__y
        return r_dict
