#!/bin/bash 
# This script will display the body of the response

if [ curl -sIX GET "$1" | grep "HTTP/1.0 200 OK" ]
then
        curl -s -X GET "$1"
fi
