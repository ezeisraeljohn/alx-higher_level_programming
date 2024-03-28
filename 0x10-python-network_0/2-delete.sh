#!/bin/bash
#Added -X DELETE to curl command
curl -sI "$1" -X DELETE | grep "Content-Length" | cut -d ":" -f2 | cut -d " " -f2
