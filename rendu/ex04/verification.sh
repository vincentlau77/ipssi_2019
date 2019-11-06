#!/bin/bash

set -e



file="efface_moi"
 if [ -e "$file" ]; then
	 rm $file
 else
	 echo "Rien à faire"
 fi
 
 exit

