#!/usr/bin/python3
"""
Task #2 - Post an email
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode('utf-8'))
