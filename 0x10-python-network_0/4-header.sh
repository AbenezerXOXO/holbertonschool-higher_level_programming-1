#!/bin/bash
# a Bash script that sends a custom header variable
curl -L -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"
