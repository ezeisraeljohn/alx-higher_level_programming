#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ Function that adds two tuples
        args:
        tuple_a
        tuple_b

        Description: This function adds two tuples where
                     The first element should be the addition of the first
                     element of each argument. The second element should
                     be the addition of the second element of each argument

        Return: The addition of the two tuples
    """

    # Make zero as default for any missing arguement in the tuple
    a_first = int(tuple_a[0]) if len(tuple_a) > 0 else 0
    a_second = int(tuple_a[1]) if len(tuple_a) > 1 else 0

    b_first = (tuple_b[0]) if len(tuple_b) > 0 else 0
    b_second = (tuple_b[1]) if len(tuple_b) > 1 else 0

    el1 = a_first + b_first
    el2 = a_second + b_second

    return (el1, el2)
