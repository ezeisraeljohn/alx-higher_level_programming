#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Function that returns the maximum number in a list

        args:
        my_list

        Return: The maximum number in a list

    """
    if not my_list:
        return None

    max = 0
    for item in my_list:
        if item > max:  # assign item to max if it is greater than max
            max = item

    return max
