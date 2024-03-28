#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen(f"{sys.argv[1]}") as response:
    print(response.headers.get('X-Request-Id'))
