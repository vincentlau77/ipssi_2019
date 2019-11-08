#!/bin/bash



result = ping -c www.google.com 
echo $result


if $ == 0; then
sed  -i '$ a commentaire' internet.log

else
echo "fail"

fi
