#!/bin/bash
# This script will send a POST request to a URL with parameters
curl -sIX POST "$1" -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
