#!/usr/bin/python3


""" This Module contains the Square class"""


class Square:
    """Defines a squre

    Attributes:
        size : The first attribute

    """
    def __init__(self, size=0):
        """Function that Initializes the square
        Args:
            size: The size of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def set_size(self, size):
        """Function that sets the size

        Args:
            size: The size of the square
        """
        self.__size = size

    def get_size(self) -> any:
        """The function that returns the size"""
        return self.__size
