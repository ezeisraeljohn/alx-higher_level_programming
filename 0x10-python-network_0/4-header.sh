#!/bin/bash
# This script will send a request to a url with a header variable X-School-User-Id: 98
curl -sH "X-School-User-Id: 98" "$1"
