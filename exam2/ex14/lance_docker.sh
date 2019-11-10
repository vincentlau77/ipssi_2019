#!/bin/bash

cd /c/Program Files/Docker Toolbox

docker build -t ipssi/ex14:1 .

docker run -it -v /tmp:/out --name container1 ipssi/ex14:1 /bin/sh 

