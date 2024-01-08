#!/usr/bin/python3

""" Module that contains an empty class"""


class BaseGeometry():
    """ An empty class
        methods:
            area(int): This is not implemented
            integer_validator(int): Function that validates integers
    """

    def area(self):
        """ Unimplemented area

            Raises:
                Exception: Always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates integer

            args:
                name(str): The string
                value(int): The int

            Raises:
                TypeError: When not int
                ValueError: when less than or equal to 0
        """
        # if not isinstance(name, str):
        #     raise TypeError("must be a string")

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
