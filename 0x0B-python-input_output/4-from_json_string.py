#!/usr/bin/python3

""" This demostrate JSON deserialization"""

import json


def from_json_string(my_str):
    """Demostrating JSON deserialization

       Args:
             my_str: Json representation of a python structure
    """
    return json.loads(my_str)
