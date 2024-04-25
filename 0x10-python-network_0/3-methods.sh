#!/bin/bash
#list all allowed methods of a url
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
