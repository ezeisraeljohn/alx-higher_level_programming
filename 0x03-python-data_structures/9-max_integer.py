#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Function that returns the maximum number in a list

        args:
        my_list

        Return: The maximum number in a list

    """
    if not my_list:
        return None

    max_value = int(my_list[0])
    for item in my_list:
        if item > max_value:  # assign item to max if it is greater than max
            max_value = item

    return max_value
