#!/usr/bin/python3
"""
Task #5 - Responce header value
"""


if __name__ == "__main__":
    import requests
    import sys

    argv = sys.argv
    r = requests.get(argv[1])
    print(r.headers["X-Request-Id"])
