#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except ValueError as error_message:
        sys.stderr.write("Exception: {}\n".format(error_message))
        return False
