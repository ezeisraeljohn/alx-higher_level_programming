#!/usr/bin/python3

""" 1-hbtn_header.py """


import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(f"{sys.argv[1]}") as response:
        print(response.headers.get('X-Request-Id'))
