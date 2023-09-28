#!/bin/bash
# display only body of a 200 status code 
curl -s -I "$1" | grep -q "HTTP/1.1 200 OK" && curl -s "$1"
