#!/usr/bin/python3

""" Module that contains The BaseGeometry class """


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
        # if not isinstance(name, str):
        #     raise TypeError("must be a string")

        if not type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ The Rectangle class

        attributes:
            width(int): the width of the rectangle
            height(int): The height of the rectangle
    """
    def __init__(self, width, height):
        """ Initializer method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
