#!/usr/bin/python3
def no_c(my_string):
    # Change the string to character of list
    char_list = list(my_string)

    # Use list comprehension to populate a new list without the c or C
    new_list = [char for char in char_list if char.lower() != 'c']
    new_string = ''.join(new_list)
    return new_string
