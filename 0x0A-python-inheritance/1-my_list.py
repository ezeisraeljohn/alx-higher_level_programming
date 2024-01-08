#!/usr/bin/python3

""" This module contains a class that inherits from the lists """


class MyList(list):
    """ Class that inherits from the list object """

    def print_sorted(self):
        """ Function that prints sorts a list """
        print(sorted(self))
