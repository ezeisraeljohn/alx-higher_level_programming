#!/usr/bin/python3
from add_0 import add


def addition():
    """ My addition function


    Returns: Nothing

    """
    a = 1
    b = 2
    _sum = add(a, b)
    print("{} + {} = {}".format(a, b, _sum))


# Do not call the function if imported
if __name__ == '__main__':
    addition()
