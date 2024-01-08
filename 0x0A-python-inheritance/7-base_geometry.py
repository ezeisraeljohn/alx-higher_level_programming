#!/usr/bin/python3

""" Module that contains an empty class"""


class BaseGeometry():
    """ An empty class
        methods:
            area(int): This is not implemented
            integer_validator(int): Function that validates integers
    """

    def area(self):
        """ Unimplemented area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates integer

            args:
                name(str): The string
                value(int): The int
        """
        name = str(name)

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
