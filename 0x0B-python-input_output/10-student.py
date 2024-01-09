#!/usr/bin/python3

""" Documentation module"""


class Student:
    """ Class Documentation """
    def __init__(self, first_name, last_name, age):
        """ Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ The Retriever """
        if attrs is None:
            # If attrs is not provided, include only attributes present
            # in __init__
            return {key: value for key, value in self.__dict__.items()
                    if key in self.__init__.__code__.co_varnames}
        else:
            # If attrs is provided, include only specified attributes
            # present in __init__
            return {attr: getattr(self, attr, None) for attr in attrs if attr
                    in self.__init__.__code__.co_varnames}
