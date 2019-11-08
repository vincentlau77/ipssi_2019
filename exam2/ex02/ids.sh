#!/bin/bash

cut -d: -f3 /etc/passwd | sort -n | uniq
