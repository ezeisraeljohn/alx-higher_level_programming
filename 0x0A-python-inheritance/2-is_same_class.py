#!/usr/bin/python3

""" Module that houses the function that checks for instances of an object """


def is_same_class(obj, a_class):
    """ Function that checks for instances of objects
        args:
            obj(object): The object to check its class
            a_class(class): The class to check with

        Return: True if the obj is an instance of a_class else False
    """

    return True if type(obj) is a_class else False
