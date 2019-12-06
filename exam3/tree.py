#!/usr/bin/python3

import sys

from math import floor
def show_tree(largeur):
    hauteur_tronc=floor((largeur/5))+1
    if (largeur%2 == 0):
        largeur=largeur+1
    if largeur <= 3:
        tronc=1
    else:
        tronc=3
    tree=""
    for i in range(1,largeur+1,2):
        tree=tree +(i*"X").center(largeur)
        tree=tree+"\n"
    for i in range(hauteur_tronc):
        if (i<hauteur_tronc-1):
            tree=tree+(tronc*"X").center(largeur)
            tree=tree+"\n"
        else:
            tree=tree+(tronc*"X").center(largeur)
    return tree
if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))
