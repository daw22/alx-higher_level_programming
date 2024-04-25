#!/bin/bash
#list all allowed methods of a url
curl -s -X OPTIONS "$1" | grep -i Allow | cut -d' ' -f2-
