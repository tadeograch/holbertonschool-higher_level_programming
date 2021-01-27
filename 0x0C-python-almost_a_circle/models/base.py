#!/usr/bin/python3
""" Base of the project """
import json
import os


class Base:
    """ start of a new class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializion of the init function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ passing dict to json string """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Json to file """
        the_list = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for i in list_objs:
                the_list.append(cls.to_dictionary(i))
        jason_strg = cls.to_json_string(the_list)
        with open(filename, 'w') as MyFile:
            MyFile.write(jason_strg)

    @staticmethod
    def from_json_string(json_string):
        """ json to string """
        if (json_string is None or len(json_string) == 0):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if (cls.__name__ == 'Rectangle'):
            dummy = cls(1, 2)
        elif (cls.__name__ == 'Square'):
            dummy = cls(3)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Creation of an instance from a JsON file """
        filename = cls.__name__ + ".json"
        MyList = []
        if os.path.isfile(filename):
            with open(filename, 'r') as MyFile:
                File = MyFile.read()
                lista = cls.from_json_string(File)
                for i in lista:
                    MyList.append(cls.create(**i))
        return MyList
