#!/bin/bash
# Send a POST request to 0.0.0.0:5000/catch_me with the appropriate data
curl -s -X PUT --data "user_id=98" 0.0.0.0:5000/catch_me
