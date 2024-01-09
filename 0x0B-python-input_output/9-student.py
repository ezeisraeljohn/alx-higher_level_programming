#!/usr/bin/python3

""" Module documentation """


class Student():
    """ Class that houses the to_json

        methods:
            to_json(): function that returns a dict
    """
    def __init__(self, first_name, last_name, age):
        """ Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Function that returns a dict"""
        return self.__dict__
