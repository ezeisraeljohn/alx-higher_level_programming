#!/usr/bin/python3

""" Demonstration of writing to files """


def write_file(filename="", text=""):
    """Function that writes to a file

       Args:
        filename(string): The file that you want to write to
        text(string): The text you want to write to the file

    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
