#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in row:
            ending = ""
            print("{:d} ".format(value), end="")
        print()
