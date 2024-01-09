#!/usr/bin/python3

""" Module that demostrate the python read method """


def read_file(filename):
    """ Function that reads a file

        Args:
            filename(file): The file to read the data from
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
