#!/usr/bin/python3
import urllib.request
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
