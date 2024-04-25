#!/bin/bash
# sends data along with request to the server
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
