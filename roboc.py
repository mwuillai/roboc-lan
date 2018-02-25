"""Module principal permettant de lancer le serveur du jeu"""

import os

from carte import carte

from labyrinthe import Labyrinthe


def main():
    """Script permettant de lancer le serveur"""
    # On charge les cartes existantes
    cartes = []
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            nom_carte = nom_fichier[:-4].lower()
            cartes.append(nom_carte)

    # Introduction du jeu avec la liste des options
    while "Choix de la carte":
        print("Bienvenue dans Roboc !")
        print("Entrez le numéro d'un labyrinthe pour commencer une partie")
        print("Labyrinthes existants :")
        for i, carte_disponible in enumerate(cartes):
            print("  {} - {}".format(i, carte_disponible))
        choix = input("Choisir un labyrinthe:")
        try:
            choix = cartes[int(choix)]
            longueur, case = carte("cartes", choix)
            labyrinthe = Labyrinthe(longueur, case)
            break
        except ValueError:
            print("erreur recommence la saisie")
            continue
    print(labyrinthe)


if __name__ == '__main__':
    main()
