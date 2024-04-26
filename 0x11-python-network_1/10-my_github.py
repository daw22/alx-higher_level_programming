#!/usr/bin/python3
"""
Task #10 - My GitHub!
"""


if __name__ == "__main__":
    import requests
    import sys

    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get("id"))
