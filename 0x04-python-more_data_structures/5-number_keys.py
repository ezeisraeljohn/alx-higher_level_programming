#!/usr/bin/python3

def number_keys(a_dictionary):
    """ Function that counts the number of keys in a dictionary

        arg:
        a_dictionary - The dictionary in question

        Return: The number of keys

    """

    if not a_dictionary:
        return 0

    return len(set(a_dictionary))
