#!/usr/bin/python3
from sys import argv


def add_line_arguments():
    arg_len = len(argv)
    sum = 0

    if arg_len > 2:
        for argc in range(1, arg_len):
            sum = sum + int(argv[argc])
        print(sum)

    if arg_len == 2:
        print(argv[1])

    if arg_len == 1:
        print(0)


if __name__ == '__main__':
    add_line_arguments()
