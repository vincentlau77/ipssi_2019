#!/usr/bin/python3

import json

with open("students.json") as json_file:
    data = json.load(json_file)
    print(data)
