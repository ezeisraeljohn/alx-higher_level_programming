#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0

    # run this block if no error (indexerror) occurs
    try:
        for index in range(x):
            strings = str(my_list[index])
            if strings.isnumeric():
                print("{:d}".format(my_list[index]), end="")
                count = count + 1
        print()

    # Otherwise run this
    except (ValueError, IndexError, TypeError):
        print()

    return count
