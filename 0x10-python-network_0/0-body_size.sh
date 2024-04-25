#!/usr/bin/bash
# a bash script that takes a URL, sends a request to that URL
curl -s "$1" | wc -c
