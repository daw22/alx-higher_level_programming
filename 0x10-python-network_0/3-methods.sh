#!/bin/bash
#list all allowed methods the server accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
