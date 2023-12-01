#!/usr/bin/python3
from sys import argv


def num_of_args():
    """ function that list out all command line arguements

    Return: Nothing

    """
    args_len = len(argv)

    # if arguement other than filename, print the index followed the the name
    if args_len == 2:
        print("{} arguement:".format(argv.index(argv[1])))
        print("{}: {}".format(argv.index(argv[1]), argv[1]))

    # if arguement is filename only, print index followed by the name
    elif args_len == 1:
        print("{} arguements.".format(argv.index(argv[0])))

    # Do this if two conditions above are not met
    else:
        print("{} arguements:".format(args_len))
        for index in range(args_len):
            print("{}: {}".format(int(argv.index(argv[index]) + 1),
                                  argv[index]))


# Don't call the function if this module is imported
if __name__ == '__main__':
    num_of_args()
