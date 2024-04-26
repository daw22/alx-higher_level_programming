#!/usr/bin/python3
"""
Task #100 - Time for an interview!
"""


if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    for i in range(0, 10):
        commit = commits[i]
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit")
                              .get("author").get("name")))
