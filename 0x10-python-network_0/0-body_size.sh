#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
# $1 : first command line argument
# -s : silent mode, -I: fetch HTTP headers of the response only without downloading the body of the response.
# -d : specifies delimeter separating fields in the input is a space
# -f2 : specifis we want to extract second field after  the space. 
curl -s $1 | wc -c
