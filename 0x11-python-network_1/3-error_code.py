#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
with : ensure the response is closed when done
response.headers: contains dictionary like object that contains the headers
.get: retrives the value associated with the key "X-Request-Id"
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
        print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
