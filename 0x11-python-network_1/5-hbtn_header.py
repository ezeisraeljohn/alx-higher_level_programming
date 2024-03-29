#!/usr/bin/python3

""" 5-hbtn_header.py """


import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
