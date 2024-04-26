#!/usr/bin/python3
"""
Task #1 - REsponce header value
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    args = sys.argv
    req = urllib.request.Request(args[1])
    with urllib.request.urlopen(req) as response:
        headers = response.info()
    print(headers['X-Request-Id'])
