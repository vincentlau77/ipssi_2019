#!/usr/bin/python3

from sys import argv
from math import floor

SECONDE = 1
MINUTE = 60 * SECONDE
HEURE = 60 * MINUTE
JOUR = 24 * HEURE
AN = 365 * JOUR


def show_sla(disponibilite):
    indisponibilite_ratio = (100 - disponibilite) / 100
    secondes_indisponibles = AN * indisponibilite_ratio
    jours = floor(secondes_indisponibles / JOUR)
    reste = secondes_indisponibles - (jours * JOUR)
    heures = floor(reste / HEURE)
    reste = reste - (heures * HEURE)
    minutes = floor(reste / MINUTE)
    reste = reste - (minutes * MINUTE)
    secondes = floor(reste / SECONDE)
    return str(jours) + 'd ' + str(heures) + 'h ' + str(minutes) + 'm ' + str(secondes) + 's'


if __name__ == "__main__":
    print(show_sla(float(argv[1])))
