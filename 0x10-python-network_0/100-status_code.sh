#!/bin/bash
# displays only the status code from a response
curl -s -o /dev/null -w "%{http_code}" "$1"
