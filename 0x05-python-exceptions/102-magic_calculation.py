#!/bin/usr/python3


def magic_calculation(a, b):
    value = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                value += (a ** b) / i
        except Exception:
            value = b + a
            break
    return value
