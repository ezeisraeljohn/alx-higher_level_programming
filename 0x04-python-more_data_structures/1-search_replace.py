#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Function that replaces occurences of an item in a list with another

        args:
        my_list - The list in question
        search - The item to be replaced in the list
        replace - The value to replace @search with

        Return: Returns a new list with the new value
    """
    if not my_list:
        return my_list

    new_list = my_list.copy()

    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace  # replaces the old element with the new one

    return new_list
