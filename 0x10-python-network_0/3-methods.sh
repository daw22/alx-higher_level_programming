#!/bin/bash
#list all allowed methods of a url
curl -s -X OPTIONS "$1" | grep "Allow" | cut -d' ' -f2-
