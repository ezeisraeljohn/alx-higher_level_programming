#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


a = 10
b = 5


def add_num():
    """ function that adds number

        Return: Nothing

    """
    number_add = add(a, b)

    print("{} + {} = {}".format(a, b, number_add))


def sub_num():
    """ function that subtracts number

        Return: Nothing

    """
    number_sub = sub(a, b)
    print("{} - {} = {}".format(a, b, number_sub))


def mul_num():
    """ function that multiplies number

    Return: Nothing

    """
    number_mul = mul(a, b)
    print("{} * {} = {}".format(a, b, number_mul))


def div_num():
    """ function that divides number

    Returns: Nothing

    """
    number_div = div(a, b)
    print("{} / {} = {}".format(a, b, number_div))


if __name__ == '__main__':
    add_num()
    sub_num()
    mul_num()
    div_num()
