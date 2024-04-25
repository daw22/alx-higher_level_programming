#!/usr/bin/env bash
# sends a DELETE request to the url at first argument and
#- displays the body of the response

curl -X DELETE "$1"
