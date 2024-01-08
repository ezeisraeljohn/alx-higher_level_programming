#!/usr/bin/python3

""" This module contains a class that inherits from the lists """


class MyList(list):
    """ Class that inherits from the list object """

    def print_sorted(self):
        """ Function that prints sorts a list """
        for i in range(len(self)):
            if not isinstance(self[i], int):
                raise TypeError("must be a list of integers")
        print(sorted(self))

