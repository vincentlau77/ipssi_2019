#!/usr/bin/python3

from datetime import datetime

def logthis(a):
    date = datetime.now()
    datedate = date.strftime("%Y-%m-%d %H:%M:%S")
    print(datedate, a)
    ecrit = datedate + " " + str(a)
    fichier = open("python.log", "a")
    fichier.write(ecrit + "\n")
    fichier.close()
