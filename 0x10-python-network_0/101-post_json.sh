#!/bin/bash
# sends a post request with a content of a file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
