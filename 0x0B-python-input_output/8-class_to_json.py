#!/usr/bin/python3

""" Module that presents a dictionary discription of a simple data list"""


def class_to_json(obj):
    """ Function that returns dic discription for serialization

        Args:
            obj: the object to use
    """
    return obj.__dict__
