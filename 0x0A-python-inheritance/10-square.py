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

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ The string function """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Class that implements the Square
        methods:
            area(int): Calculate the area of the square

        attributes:
            size(int): The size of the square
    """
    def __init__(self, size):
        """ Initializer method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
