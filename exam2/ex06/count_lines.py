#!/usr/bin/python3


import sys



def file_lengthy(sys.argv[1]):
        with open(sys.argv[1]) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file:", file_lengthy(sys.argv[1]))
