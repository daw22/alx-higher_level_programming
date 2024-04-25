#!/usr/bin/env bash
# a bash script that takes a URL, sends a request to that URL
#- and display the size of the body of the responce


curl -sI $1 | grep -i content-Length | cur -d' ' -f2-
