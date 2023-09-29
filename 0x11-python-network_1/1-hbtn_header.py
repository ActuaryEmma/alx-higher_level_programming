#!/usr/bin/python3
import urllib.request
import sys
"""
script that fetches https://alx-intranet.hbtn.io/status
with : ensure the response is closed when done
response.headers: contains dictionary like object that contains the headers
.get: retrives the value associated with the key "X-Request-Id"
"""

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
