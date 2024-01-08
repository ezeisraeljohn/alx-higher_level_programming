#!/usr/bin/python3

""" Module that contains a function that checks for instance of a class"""


def is_kind_of_class(obj, a_class):
    """ Function that checks if an object is an instance of a class or it
        instance of an inherited class

        args:
            obj(object): The object
            a_class(class): The class to check with

        Returns: True if it the instance of the class or the superclass else
                 returns false
    """
    return True if isinstance(obj, a_class) else False
