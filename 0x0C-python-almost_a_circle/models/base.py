#!/usr/bin/python3

""" The Module Documentation """


import json
import os


class Base():
    """ The base class of this project

        Attributes:
            class_attributes:
                __nb_objects(int): The first instance variable

            instance_attributes:
                identity(int): The first instance attribute of this class
    """
    __nb_objects = 0

    def __init__(self, identity=None):
        """ Initializer Method"""
        if identity is not None:
            self.id = identity
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list_dictionaries to json serializaion"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class that saves to a file
            Args:
                list_objs: The list of objects to be converted to dictionary
        """
        dic_list = [obj.to_dictionary() for obj in list_objs]
        cls.to_json_string(dic_list)

        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as file:
            json.dump(dic_list, file)

    @staticmethod
    def from_json_string(json_string):
        """ Deserializes a json string

            Args:
                json_string: The Json strings
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Added the create method """
        dummy = cls(1, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        if not os.path.isfile(f'{cls.__name__}.json'):
            return []
        else:
            with open(f'{cls.__name__}.json', 'r', encoding='utf-8') as file:
                instances = file.readline()
                cls.from_json_string(instances)
                return [instance for instance in instances]
