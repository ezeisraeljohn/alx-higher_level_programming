#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ Function that deletes an item of a list at a given idx position
        arg:
        my_list

        Return: The list with the item removed
    """
    if not my_list:
        return my_list  # return the list if empty

    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
