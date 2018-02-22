# -*-coding:Utf-8 -*

import os

from random import randint

from objet import Objet

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

    def __repr__(self):
        grille_complete = ""
        for i, case in enumerate(self.grille):
            self.calcxy(i)
            grille_complete += (self.grille[self.x, self.y].valeur)
        return grille_complete

    def placement(self, nombre_joueur):
        i = 0  # iteration à réaliser pour placer tous les joueurs --> une iteration par joueur
        while i < nombre_joueur:
            i += 1
            emplacement_possible = []
            for cle in self.grille.keys():
                if self.grille[cle].valeur == " ":
                    emplacement_possible.append(cle)
            position_de_x = emplacement_possible[randint(
                0, len(emplacement_possible) - 1)]
            self.grille[position_de_x].positionnement_joueur(i)
            self.X.append(position_de_x)

    def affichage_client(self, joueur_en_cours):
        """Permet d'afficher le plan pour un joueur 'client' l'argument joueur en cours 
        dois prendre le numéro du joueur à joueur en partant de 0. Ainsi la méthode affichera une carte
        ou les autres joueurs apparaitrons comme étant 'x' et le joueur en cours comme étant 'X'"""
        self.grille[self.X[joueur_en_cours]].joueur_en_cours()
        print(self)
        for joueur in self.X:
            self.grille[joueur].joueur_desac()

    """-------------------------------------------------------------------------------------------------------------------------------
    Définition des actions de déplacement, sur cette class carte j'insère également les actions permettant à un personnage de se déplacer.
    Cela se fera en 3 étapes, d'abord déclaration de l'intention du mouvement, vérification de la validité du mouvement, réalisation du mouvement.
    ----------------------------------------------------------------------------------------------------------------------------------"""

    def deplacement(self, orientation):
        if orientation == "O":
            cible = (self.X[0] - 1, self.X[1])
        elif orientation == "E":
            cible = (self.X[0] + 1, self.X[1])
        elif orientation == "N":
            cible = (self.X[0], self.X[1] - 1)
        elif orientation == "S":
            cible = (self.X[0], self.X[1] + 1)
        else:
            return "Erreur : mauvaise saisie"
        etatcible = self.grille[cible]
        if etatcible == " " or etatcible == ".":
            # L'emplacement de X prend la valeur du dernier mouvement
            self.grille[self.X] = self.mvtprecedent
            # Le mouvement précédent devient la valeur de la case à venir
            self.mvtprecedent = etatcible
            self.grille[cible] = "X"  # La valeur de la case cible devient X
            self.X = cible
        elif etatcible == "O":
            print("poum! Un mur ça fait mal")
        elif etatcible == "U":
            return "WIN"
