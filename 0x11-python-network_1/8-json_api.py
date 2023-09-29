#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
requests- interact with web services, API or websites by making HTTP requests
requests.get : retrive content of a web page
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    letter = "" if len(argv) == 1 else argv[1]
    req = requests.post(url, {"q": letter})

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
