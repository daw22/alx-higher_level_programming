#!/usr/bin/python3
"""
Task #8- Search api
"""


if __name__ = "__main__":
    import sys
    import requsts

    url = "http://0.0.0.0:5000/search_user"
    query = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post(url, data={'q': query})
    try:
        j_data = r.json()
        if not j_data:
            print("No result")
        else:
            print("[{}] {}".format(j_data.get("id"), j_data.get("name")))
    except Exception:
        print("Not a valid Json")
