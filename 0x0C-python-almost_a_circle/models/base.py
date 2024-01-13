#!/usr/bin/python3

""" The Module Documentation """


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
