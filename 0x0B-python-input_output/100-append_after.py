#!/usr/bin/python3

""" The documentation writing file to specific lines"""


def append_after(filename="", search_string="", new_string=""):
    """ Appends a new line of string after a specified line

        Args:
            search_string(): The specified string to search for
            new_string(): The new string to place below the line

    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
