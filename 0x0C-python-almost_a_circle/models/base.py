#!/usr/bin/python3
'''Base class'''
import json
import os


class Base:
    '''This class will be the “base” of all other classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Id instantation'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''
        if list_objs is not None:
            new_list = []
            filename = cls.__name__ + ".json"
            for i in list_objs:
                new_list.append(i.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, "r") as f:
            r = f.read()
            lista = cls.from_json_string(r)
            new_l = []
            for l in lista:
                new_l.append(cls.create(**l))
        return new_l
