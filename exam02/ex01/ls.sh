#!/bin/bash
if [ -e "$1" ]; then
        echo "ls ok"
        ls -la / $1 >> /tmp/ls.log
else
        echo "ls FAIL"
        $1 2>> /tmp/ls_err.log
fi
