#!/usr/bin/python3

"""This module makes use of the getters and setters"""


class Square:
    """Class that handles square methods

    Attribute:
        size(int, optional): The length of the square

    """
    def __init__(self, size=0):
        """Initialize the size"""
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        "Sets the size of the square"
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size
