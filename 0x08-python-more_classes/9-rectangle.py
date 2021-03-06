#!/usr/bin/python3
'''Simple rectangle'''


class Rectangle:
    '''Class that defines a rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''width and height instantiation'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            per = 0
        else:
            per = (self.__width * 2) + (self.__height * 2)
        return per

    def __str__(self):
        '''return the rectangle with the character #'''
        rectangle = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rectangle += str(self.print_symbol)
                if i != self.__height - 1:
                    rectangle += "\n"
        return rectangle

    def __repr__(self):
        '''return a string representation of the rectangle'''
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        '''Prints a message when an instance of Rectangle is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Defines a square'''
        new = Rectangle(size, size)
        return new
