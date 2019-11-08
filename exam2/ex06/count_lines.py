#!/usr/bin/python3


import sys

with open(sys.argv[1]) as f:
    for i, l in enumerate(f):
        pass
    print("file has: ", str(i+1), "lines")
