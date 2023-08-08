#!/usr/bin/python3
def uppercase(str):
    for s in str:
       st = chr(ord(s) - 32) if ord(s) >= 97 and ord(s) <= 122 else s
       print("{:s}".format(st), end="")
    print("")
