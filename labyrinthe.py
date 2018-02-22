# -*-coding:Utf-8 -*

"""Ce module contient les fonctions permettant de se déplacer
dans le labyrinthe"""

from case import cases
from random import randint

class Labyrinthe:

    """Le labyrinthe permet d'intéragir avec les différentes
    case qui le compose, les actions des jouers se feront
    par son intermédiaire. Pour cela il contient des
    attribut avec toutes les positions des cases et toutes
    les positions des joueurs"""

    longueur = 0
    joueurs = []
    cases = {}

    def __init__(self, longueur, * case):
        """L'initialisation du labyrinthe prend en attribut
        la liste des cases qui le compose. Longueur prend
        la longueur d'une ligne"""
        self.longueur = longueur
        for i, case in enumerate(case):
            self.cases[(self.x(i), self.y(i))] = cases(case)

    def x(self, i):
        """Méthode permettant de calculer la position x d'une case
        en fonction du nombre d'itération réaliser."""
        x = i - (i // self.longueur) * self.longueur
        return x

    def y(self, i):
        """Méthode permettant de calculer la position x d'une case
        en fonction du nombre d'itération réaliser."""
        y = i // self.longueur
        return y

    def placement(self, nombre_joueur):
        i = 0  # iteration à réaliser pour placer tous les joueurs
        while i < nombre_joueur:
            i += 1
            emplacement_possible = []
            for cle in self.cases.keys():
                if self.cases[cle].valeur == " ":
                    emplacement_possible.append(cle)
            position_de_x = emplacement_possible[randint(
                0, len(emplacement_possible) - 1)]
            self.cases[position_de_x].positionnement_joueur(i)
            self.joueurs.append(position_de_x)


""" Ancienne version du labyrinthe à supprimer
def Labyrinthe(carte, choix):
    while True:
        win = False
        if len(choix) > 1:
            try:
                iteration = int(choix[1:])
            except:
                iteration = 1
        else:
            iteration = 1
        while iteration > 0:
            if carte.deplacement(choix[0]) == "WIN":
                win = True
            iteration = iteration - 1
        if win == True:
            print("Bravo ! C'est gagné")
            break
        else:
            print("-------------------")
            print(carte)
            print("-------------------")"""
