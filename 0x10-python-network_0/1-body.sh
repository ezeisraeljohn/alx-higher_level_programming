#!/bin/bash 
# This script will display the body of the response
curll=$(curl -sI "$1" | grep "HTTP/1.1 200 OK" |cut -d " " -f2)

if [ "$curll" = "200" ]
then
       curl -s -X GET "$1"
fi
