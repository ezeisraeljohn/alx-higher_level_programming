#!/usr/bin/python3

""" This will grab commits of a user from github"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    for i in r.json()[:10]:
        print(i.get('sha'), i.get('commit').get('author').get('name'))
