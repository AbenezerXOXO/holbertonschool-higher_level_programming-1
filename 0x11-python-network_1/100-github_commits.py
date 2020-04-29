#!/usr/bin/python3
"""
a Python script that uses github api to list 10 commits
"""
import requests
import sys


if __name__ == '__main__':
    github = sys.argv[1] + '/' + sys.argv[2]
    url = 'https://api.github.com/repos/' + github + '/commits'
    r = requests.get(url)
    for i in r.json()[:10]:
        sha = i['sha']
        auth = i['commit']['author']['name']
        print("{}: {}".format(sha, auth))
