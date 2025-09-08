#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    lenght = len(sentence)
    first = sentence[0]
    return (lenght, first)
