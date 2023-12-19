#!/usr/bin/python3


""" This Module contains the Square class That calculates the area of a
    square
"""


class Square:
    """Defines a squre

    Attributes:
        size(int, optional) : The length of the square

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

    def area(self):
        """Calculate the area of a square"""
        return self.__size * self.__size
