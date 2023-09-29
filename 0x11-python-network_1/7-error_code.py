#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
requests- interact with web services, API or websites by making HTTP requests
requests.get : retrive content of a web page
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            html = response.text
        print(html)
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'status_code'):
            print("Error code:", e.response.status_code)
        else:
            print("Error Code:", e)
