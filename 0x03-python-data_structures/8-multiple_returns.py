#!/usr/bin/python3

def multiple_returns(sentence):
    """ Function that returns multiple values as a tuple

        arg:
        sentence

        Return: The tuple
    """
    # first character if non-empty else None
    first_char = sentence[0] if sentence else None

    return (len(sentence), first_char)
