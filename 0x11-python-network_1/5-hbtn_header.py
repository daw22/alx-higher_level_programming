#!/usr/bin/python3
"""
Task #5 - Responce header value
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
