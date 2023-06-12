#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    for word in range(0, length):
        if (sentence == ""):
            letter = None
        else:
            letter = sentence[0]
    return (length, letter)
