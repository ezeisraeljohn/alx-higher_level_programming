#!/usr/bin/python3

"""This module contains the function that prints a square in # representation
"""

def print_square(size):
    """"Function that prints a square in '#' form 

        args:
            size(int | float): The size of the square

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(int(size)):
        for _ in range(int(size)):
            print("#", end="")
        print()