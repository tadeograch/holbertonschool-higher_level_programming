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
        '''__str__ method'''
        text = "[Square] ({}) {}/{} - {}"
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        return (text.format(a, b, c, d))

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
        '''Updates attributes'''
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                if not type(args[1]) is int:
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = args[1]
                self.__height = args[1]
            if len(args) > 2:
                if not type(args[2]) is int:
                    raise TypeError("x must be an integer")
                if args[2] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[2]
            if len(args) > 3:
                if not type(args[3]) is int:
                    raise TypeError("y must be an integer")
                if args[3] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[3]
        else:
            for key, val in kwargs.items():
                if not type(val) is int:
                    raise TypeError("{} must be an integer".format(key))
                if key == "id":
                    self.id = val
                if key == "size":
                    if val <= 0:
                        raise ValueError("{} must be > 0".format(key))
                    self.__width = val
                    self.__height = val
                if key == "x":
                    if val < 0:
                        raise ValueError("{} must be >= 0".format(key))
                    self.__x = val
                if key == "y":
                    if val < 0:
                        raise ValueError("{} must be >= 0".format(key))
                    self.__y = val

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square'''
        r_dict = {}
        r_dict['id'] = self.id
        r_dict['size'] = self.__width
        r_dict['x'] = self.__x
        r_dict['y'] = self.__y
        return r_dict
