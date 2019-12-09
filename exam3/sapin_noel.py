#!/usr/bin/python3

import sys
from math import floor
import random

def show_tree(largeur):
    hauteur_tronc=floor((largeur/5))+1
    if (largeur%2 == 0):
        largeur=largeur+1
    if largeur <= 3:
        tronc=1
    else:
        tronc=3
    tree=""
    nb_boule=floor(random.random()*largeur)
    for i in range(1,largeur+1,2):
        tree=tree +(i*"x").center(largeur)
        tree=tree+"\n"
    chaine= list(tree)
    for i in range(len(chaine)):
        if (random.random() < largeur/100):
            if (chaine[i] == 'x'):
                chaine[i] = 'O'
    tree= "".join(chaine)
    for i in range(hauteur_tronc):
        if (i<hauteur_tronc-1):
            tree=tree+(tronc*"x").center(largeur)
            tree=tree+"\n"
        else:
            tree=tree+(tronc*"x").center(largeur)  
    return tree

if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))
