#!/usr/bin/env bash
#list all allowed methods of a url

curl -X OPTIONS -sI "$1" | grep -i Allow | cut -d' ' -f2-
