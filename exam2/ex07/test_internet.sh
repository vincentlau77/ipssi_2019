#!/bin/bash

if [ -z www.google.com ] || curl -s -I www.google.com >/dev/null ;then
        echo "$(date '+%Y-%m-%d %H:%M:%S') internet OK" >> internet.log
else
        echo "$(date '+%Y-%m-%d %H:%M:%S') internet FAIL" >> internet.log
fi

exit
