# -*-coding:Utf-8 -*

import os

from labyrinthe import Labyrinthe

"""Ce module contient la classe Carte."""


class Carte:
    """Objet de transition entre un fichier et un labyrinthe.
    Le principe est qu'il doit lire un fichier pour le découper
    avant d'initialiser notre labyrinthe puis nos cases"""

    labyrinthe = ""  # variable qui contient le nom du labyrinthe

    def __init__(self, nom, dossier, chaine):
        """Initialisation du labyrinthe à partir du fichier carte
        le premier argument prend le nom à donner du labyrinthe
        le second argument prend le nom du dossier ou se trouve les
        labyrinthe. Le troisième prend le nom du fichier"""
        with open(os.path.join(dossier, "{}.txt".format(chaine)), "r") as laby:
            labyBrut = laby.readline()
            longueur = len(labyBrut)
            labyBrut += laby.read()
        nom = Labyrinthe(longueur, labyBrut)

    def calcxy(self, i):
        """Calcul x et y en fonction de la longueur du labyrinthe fonction
        à utiliser dans le cadre d'une boucle pour mettre à jour l'attribut
        à chaque affectation de case"""
        self.x = i - (i // self.longueur) * self.longueur
        self.y = i // self.longueur
