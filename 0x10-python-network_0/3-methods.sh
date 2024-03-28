#!/bin/bash
# This script will display allowed methods
curl -siIX OPTIONS "$1" | grep "Allow"|cut -d " " -f2-
