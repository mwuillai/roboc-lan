# -*-coding:Utf-8 -*

"""Ce module contient la classe permettant
de générer les cases du labyrinthe. Ces cases
contiennent les caractéristiques permettant de
savoir comment intéragir avec"""


class Cases:
    """Class qui permet de générer les cases du
    labyrinthe."""

    valeur = " "  # Valeur de la case
    bloquant = False  # Indique si la case doit bloquer le joueur
    valeurPrecedente = " "  # Cette valeur est la dernière position de la case

    def __init__(self, valeur):
        self.valeur = valeur
        if valeur == "O":
            self.bloquant = True
