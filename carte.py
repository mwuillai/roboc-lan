"""Ce module contient la methode Carte."""
# -*-coding:Utf-8 -*

import os


def carte(dossier, chaine):
    """Initialisation du labyrinthe à partir du fichier carte
    le premier argument prend le nom à donner du labyrinthe
    le second argument prend le nom du dossier ou se trouve les
    labyrinthe. Le troisième prend le nom du fichier"""
    with open(os.path.join(dossier, "{}.txt".format(chaine)), "r") as laby:
        laby_brut = laby.readline()
        longueur = len(laby_brut)
        laby_brut += laby.read()
    return longueur, laby_brut
