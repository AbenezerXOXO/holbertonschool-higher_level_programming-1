#!/usr/bin/python3
"""
a Python script that uses github api to list 10 commits
"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/repos/' + sys.argv[1] + '/' + sys.argv[2] + \
          '/commits'
    r = requests.get(url)
    for i in r.json()[:10]:
        print("{}: {}".format(i['sha'],
                              i['commit']['author']['name']))
