#!/usr/bin/python3

teststr = 'image:'

images = []

with open('docker-compose.yml') as f:
   for line in f:
       if teststr in line:
           print(line.strip().split()[1])

f.close
