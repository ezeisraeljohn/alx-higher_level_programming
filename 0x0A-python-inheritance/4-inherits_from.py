#!/usr/bin/python3
"""Module that contains the function that prints check for instance of class"""


def inherits_from(obj, a_class):

    """ Function that checks if an object is an instance of a class or it
        instance of an inherited class

        args:
            obj(object): The object
            a_class(class): The class to check with

        Returns: True if it the instance of the class or the superclass else
                 returns false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
