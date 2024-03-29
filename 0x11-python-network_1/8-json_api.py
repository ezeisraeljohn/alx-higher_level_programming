#!/usr/bin/python3

""" 8-json_api.py """


import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

    if not r.json():
        print("Not a valid JSON")
    if type(r.json()) is dict:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
