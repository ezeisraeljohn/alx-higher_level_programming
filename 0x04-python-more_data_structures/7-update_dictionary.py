#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """ Function that updates/overites a key in a dictionary

        args:
        a_dictionary - The dictionary in question
        key - The key to overwite with
        value - The value of the key

        Return: The updated dictionary

    """
    a_dictionary[key] = value

    return a_dictionary
