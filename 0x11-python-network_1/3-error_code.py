#!/usr/bin/python3

""" This handles error code """

import sys
import urllib.request

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
