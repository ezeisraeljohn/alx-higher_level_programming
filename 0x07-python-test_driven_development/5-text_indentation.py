#!/usr/bin/python3
""" Module that proper indents a text """


def text_indentation(text):
    """Function that prints a formated and well indented text

        args:
            text(str): The text which we want to properly indent
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_list = list(text)

    for i in range(len(new_list)):
        if new_list[i] in ('.', '?', ':'):
            new_list[i] = '\n \n'

    text = ''.join(new_list)

    print(text, end="")
