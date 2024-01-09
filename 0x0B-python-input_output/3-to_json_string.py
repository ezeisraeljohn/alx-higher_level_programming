#!/usr/bin/python3


""" Representation of JSON Serialization"""

import json


def to_json_string(my_obj):
    """ Function that serializes a json object

        Args:
            my_obj(JSON): The json object
    """
    return json.dumps(my_obj)
