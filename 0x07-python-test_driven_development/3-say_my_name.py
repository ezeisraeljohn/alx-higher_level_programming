#!/usr/bin/python3
"""Module that contain function that prints someone's name
    This module doesn't allow importing another module based on instruction
"""


def say_my_name(first_name, last_name=""):
    """Function that prints someone's name

        args:
            first_name(str): The first name of the person
            last_name(str): The second string of the person

        Raises:
            TypeError: This function raises a type error if any of the
                       arguements passed to it is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
