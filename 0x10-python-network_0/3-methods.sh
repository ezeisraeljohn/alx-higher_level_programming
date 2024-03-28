#!/bin/bash
# This script will display allowed methods
curl -sI "$1" | grep "Allow"
