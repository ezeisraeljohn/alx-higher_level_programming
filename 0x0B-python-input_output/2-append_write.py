#!/usr/bin/python3

""" Demostrating appending to a file """


def append_write(filename="", text=""):
    """ Function that appends strings to a file

     Args:
        filename(string): The file that you want to write to
        text(string): The text you want to write to the file

    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
