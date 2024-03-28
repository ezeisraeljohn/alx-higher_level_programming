#!/bin/bash
# This script will send a POST request to a URL with parameters
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"