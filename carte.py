# -*-coding:Utf-8 -*

import os

from random import randint

"""Ce module contient la classe Carte."""


class Carte:
    """Objet de transition entre un fichier et un labyrinthe.
    Le principe est qu'il doit lire un fichier pour le découper
    avant d'initialiser notre labyrinthe puis nos cases"""

    grille = {}
    x = 0  # variable dynamique indiquant la position x de la case
    y = 0  # variable dynamique indiquant la position x de la case
    X = []  # position des joueurs dans le labyrinthe
    longueur = 0  # longueur du labyrinthe
    mvtprecedent = " "  # contient le contenu de la case ou se trouvait x avant le déplacement

    def __init__(self, nom, dossier, chaine):
        """Initialisation du labyrinthe à partir du fichier carte affecte
        une position x et y à chaque caractère du labyrinthe"""
        with open(os.path.join(dossier, "{}.txt".format(chaine)), "r") as laby:
            labyBrut = laby.readline()
            self.longueur = len(labyBrut)
            labyBrut += laby.read()
            grille = {}
            for i, case in enumerate(labyBrut):
                self.calcxy(i)
                objet = Objet("0", case)
                grille[self.x, self.y] = objet
        self.nom = nom
        self.grille = grille

    def calcxy(self, i):
        """Calcul x et y en fonction de la longueur du labyrinthe fonction
        à utiliser dans le cadre d'une boucle pour mettre à jour l'attribut à chaque affectation de case"""
        self.x = i - (i // self.longueur) * self.longueur
        self.y = i // self.longueur
