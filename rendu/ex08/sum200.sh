#!/bin/bash

while read n; do
	sum=$(($sum+$n));
done
echo $sum

exit
