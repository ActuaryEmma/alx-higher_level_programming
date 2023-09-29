#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
requests- interact with web services, API or websites by making HTTP requests
requests.get : retrive content of a web page
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
try:
    with requests.get(url) as response:
        response.raise_for_status()
        html = response.text
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
except requests.exceptions.RequestException as e:
    print("Error:", e)
