#!/usr/bin/python3


def element_at(my_list, idx) -> int:
    if idx < 0 or idx >= len(my_list):
        return None  # Item does not exist
    return my_list.pop(idx)
