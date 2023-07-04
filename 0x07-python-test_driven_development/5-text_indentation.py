#!/usr/bin/python3
def text_indentation(text):
    """ fuction to strip words from a string"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    word = ''
    for s in range(len(text)):
        if text[s] == '.' or text[s] == '?' or text[s] == ':':
            word += text[s]
            print(word.strip())
            print()
            word = ''
        else:
            word += text[s]
    if word:
        print(word.strip())
