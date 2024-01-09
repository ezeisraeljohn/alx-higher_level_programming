#!/usr/bin/python3

""" Documentation a JSON Serialization"""

import json


def save_to_json_file(my_obj, filename):
    """Function that implements the json serialization

       Args:
            my_obj: The json representation
            filename: The file to write the json representation to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
