#!/usr/bin/python3

"""This module contains function that adds two numbers"""

def add_integer(a, b=98):
    """ Function that adds two numbers

        args:
            num1 (int): The first number to be added
            num2 (int): The second number to be added
        
        Description:
            The function adds two numbers only if the two numbers passed into
            it are float or int. if it is a float, it is first typcasted into an integer and then added.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    convert_to_int = (int(a), int(b))

    return convert_to_int[0] + convert_to_int[1]
