#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ function to tell a number is a multiple of 2

    args:
    my_list[]

    Return: The a new list containing true or false values

    """
    new_list = []

    for item in my_list:
        check = int(item) % 2 == 0
        new_list.append(check)

    return new_list
