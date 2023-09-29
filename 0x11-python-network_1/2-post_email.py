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
    email = sys.argv[2]
    params = {'email': email}
    post_data = urllib.parse.urlencode(params)
    post_data = post_data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data=post_data, method='POST')
    with urllib.request.urlopen(req) as response:
        data = response.read()
    print(data.decode('utf-8'))
