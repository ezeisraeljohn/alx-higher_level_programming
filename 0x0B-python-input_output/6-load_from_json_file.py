#!/usr/bin/python3


""" Documentation for JSON deserialization """


import json


def load_from_json_file(filename):
    """ Function documentation

        Args:
            filename(name):

    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
