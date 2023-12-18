#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0

    for i in my_list:
        count = count + 1

    try:
        for index in range(x):
            print(f"{my_list[index]}", end="")
        print()

    except IndexError:
        print()

    count = x if x < count else count

    return count
