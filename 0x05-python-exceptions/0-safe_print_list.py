#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0

    for i in my_list:
        count = count + 1  # Get the length of the list

    # run this block if no error (indexerror) occurs
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
        print()

    # Otherwise run this
    except IndexError:
        print()

    # get the number of element printed
    count = x if x < count else count

    return count
