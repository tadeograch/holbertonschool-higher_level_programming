#!/usr/bin/python3
'''Student class'''


class Student:
    '''Defines a student'''
    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student instance'''
        flag = 0
        my_dict = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return my_dict
        else:
            return self.__dict__
