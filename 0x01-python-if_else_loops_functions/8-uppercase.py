#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            print("{:s}".format(chr(ord(s) - 32)), end="")
        else:
            print("{:s}".format(s), end="")
    print("")
