#!/usr/bin/python3

""" 2-post_email.py """


import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(f"{sys.argv[1]}", data=f"email={sys.argv[2]}".
                                encode('utf-8')) as response:
        print(response.read().decode('utf-8'))
