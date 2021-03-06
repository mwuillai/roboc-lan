# -*-coding:Utf-8 -*

"""Ce module contient les fonctions permettant de se déplacer
dans le labyrinthe"""

from random import randint
from case import Cases


class Labyrinthe:

    """Le labyrinthe permet d'intéragir avec les différentes
    case qui le compose, les actions des jouers se feront
    par son intermédiaire. Pour cela il contient des
    attribut avec toutes les positions des cases et toutes
    les positions des joueurs"""

    longueur = 0
    joueurs = []
    cases = {}

    def __init__(self, longueur, cases):
        """L'initialisation du labyrinthe prend en attribut
        la liste des cases qui le compose. Longueur prend
        la longueur d'une ligne"""
        self.longueur = longueur
        for i, case in enumerate(cases):
            self.cases[(self.valeur_x(i), self.valeur_y(i))] = Cases(case)

    def __repr__(self):
        labyrinthe = ""
        iteration = 0
        while iteration < len(self.cases):
            labyrinthe += (
                self.cases[self.valeur_x(iteration), self.valeur_y(iteration)].
                valeur)
            iteration += 1
        return labyrinthe

    def valeur_x(self, i):
        """Méthode permettant de calculer la position x d'une case
        en fonction du nombre d'itération réaliser."""
        valeur_x = i - (i // self.longueur) * self.longueur
        return valeur_x

    def valeur_y(self, i):
        """Méthode permettant de calculer la position x d'une case
        en fonction du nombre d'itération réaliser."""
        valeur_y = i // self.longueur
        return valeur_y

    def placement(self, nombre_joueur):
        """Méthode permettant de placer les joueurs sur la carte.
        Elle prend en argument le nombre de joueur à placer sur
        la carte"""
        i = 0  # iteration à réaliser pour placer tous les joueurs
        while i < nombre_joueur:
            i += 1
            emplacement_possible = []
            for cle in self.cases:
                if self.cases[cle].valeur == " ":
                    emplacement_possible.append(cle)
            position_de_x = emplacement_possible[randint(
                0, len(emplacement_possible) - 1)]
            self.cases[position_de_x].positionnement_joueur()
            self.joueurs.append(position_de_x)

    def deplacement(self, direction, joueur):
        """Méthode de déplacement. direction prend la valeur
        de la direction souhaité, n, s, o ou e. joueur prend
        la valeur du numéro du joueur qui doit jouer"""

        position_joueur = self.joueurs[joueur]
        valeur_de_x, valeur_de_y = position_joueur
        position_joueur = self.cases[(position_joueur)]
        # import pdb; pdb.set_trace()
        if direction == "o":
            destination_x = valeur_de_x - 1
            destination = (destination_x, valeur_de_y)
        if direction == "e":
            destination_x = valeur_de_x + 1
            destination = (destination_x, valeur_de_y)
        if direction == "n":
            destination_y = valeur_de_y - 1
            destination = (valeur_de_x, destination_y)
        if direction == "s":
            destination_y = valeur_de_y + 1
            destination = (valeur_de_x, destination_y)
        if direction not in "nseo":
            print("Mauvaise commande")
        case_destination = self.cases[destination]
        if case_destination.bloquant is False:
            position_joueur.mouvement_sortant()
            case_destination.mouvement_entrant()
            self.joueurs[joueur] = destination
        else:
            print("Deplacement impossible")
