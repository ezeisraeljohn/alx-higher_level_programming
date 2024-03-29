#!/usr/bin/python3

""" 7-error_code.py """


import sys
import requests

if __name__ == "__main__":
        r = requests.get(sys.argv[1])
        if r.status_code >= 400:
                print("Error code: {}".format(r.status_code))
        else:
                print(r.text)
