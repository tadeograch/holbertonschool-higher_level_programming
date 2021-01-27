#!/usr/bin/python3
'''Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle that inherits from base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantation of attributes'''
        super().__init__(id)
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not type(x) is int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not type(y) is int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if not type(x) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if not type(width) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns the area'''
        return self.__width * self.__height

    def display(self):
        '''Prints the rectangle with the "#" caracter'''
        for a in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for b in range(0, self.__x):
                    print(end=" ")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''__str__ method'''
        text = "[Rectangle] ({}) {}/{} - {}/{}"
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        return (text.format(a, b, c, d, e))

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
            if len(args) > 2:
                if not type(args[2]) is int:
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = args[2]
            if len(args) > 3:
                if not type(args[3]) is int:
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[3]
            if len(args) > 4:
                if not type(args[4]) is int:
                    raise TypeError("y must be an integer")
                if args[4] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[4]
        else:
            for key, val in kwargs.items():
                if not type(val) is int:
                    raise TypeError("{} must be an integer".format(key))
                if key == "id":
                    self.id = val
                if key == "width":
                    if val <= 0:
                        raise ValueError("{} must be > 0".format(key))
                    self.__width = val
                if key == "height":
                    if val <= 0:
                        raise ValueError("{} must be > 0".format(key))
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
        '''Returns the dictionary representation of a Rectangle'''
        r_dict = {}
        r_dict['id'] = self.id
        r_dict['width'] = self.__width
        r_dict['height'] = self.__height
        r_dict['x'] = self.__x
        r_dict['y'] = self.__y
        return r_dict
