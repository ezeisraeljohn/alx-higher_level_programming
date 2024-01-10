#!/usr/bin/python3


""" Documentation module"""


def pascal_triangle(n):

    """ Function that defines the pascal triangle """

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        if i > 0:
            row.append(1)  # Last element of each row is always 1

        triangle.append(row)

    return triangle
