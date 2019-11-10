#!/usr/bin/python3

import hashlib

a = hashlib.md5("ipssi".encode()).hexdigest()

print('md5 "ipssi" : ', a)

def compare_pass(test):
    b = hashlib.md5(test.encode()).hexdigest()
    print('md5    pass :', b)
    if b == a:
        print('login ok')
    else:
        print('login failed')
