#!/bin/bash
# sends data along with request to the server
curl -s -X POST -d "email=test@gmail.com&subject=I will always be there for PLD" "$1"
