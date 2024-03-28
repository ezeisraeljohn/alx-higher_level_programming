#!/bin/bash
# Prints the status code
curl -w "%{http_code}" -s -o /dev/null "$1"