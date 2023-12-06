#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ Function that adds item of a list without adding a duplicate of it

        args:
        my_list - The list in question

        Return: The sum of the list

    """
    if not my_list:
        return my_list

    list_sum = 0

    # make create a set of my_list
    my_list_set = set(my_list)

    for item in my_list_set:
        list_sum += int(item)

    return list_sum
