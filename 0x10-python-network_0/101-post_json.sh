#!/bin/bash
# This script will send a POST request to a URL with parameters
curl -d @"$2"-X POST "$1"
