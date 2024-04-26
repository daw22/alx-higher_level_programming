#!/usr/bin/python3
"""
Task #3 - Error code
"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    argv = sys.argv
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.status)
