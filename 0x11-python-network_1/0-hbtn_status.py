#!/usr/bin/python3
"""
Task #0 - What is my Status?
"""

if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as responce:
        body = responce.read()
    print("Body response")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
