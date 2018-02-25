# -*-coding:Utf-8 -*

"""Ce module contient la classe permettant
de générer les cases du labyrinthe. Ces cases
contiennent les caractéristiques permettant de
savoir comment intéragir avec"""


class Cases:
    """Class qui permet de générer les cases du
    labyrinthe."""

    valeur = " "  # Valeur de la case
    _bloquant = False  # Indique si la case doit bloquer le joueur
    valeur_precedente = " "  # Cette valeur est la dernière position de la case
    joueur = False  # Devient True si un joueur est sur la case

    def __init__(self, valeur):
        self.valeur = valeur
        if valeur == "O":
            self._bloquant = True

    def mouvement_entrant(self):
        """Méthode à employer lorsqu'un joueur veux entrer sur la case
        Si le mouvement est possible la méthode renvoie True et la
        valeur de la case devient X. valeurPrecedente devient l'ancienne
        valeur de la case avant l'entrée de X sur cette case"""
        if self._bloquant:
            return False
        self.valeur_precedente = self.valeur
        self.valeur = "X"
        return True

    def mouvement_sortant(self):
        """Méthode permettant d'indiquer qu'un joueur sors de la case"""
        self.valeur = self.valeur_precedente

    def positionnement_joueur(self):
        """Méthode permettant de positionner un jouer sur cette case"""
        self.valeur = "x"
        self.joueur = "True"

    def joueur_en_cours(self):
        """Méthode indiquant que cette case contient le joueur en
        train de jouer, il a donc la valeur X"""
        self.valeur = "X"

    def joueur_standby(self):
        """Méthode indiquant que le joueur sur cette case n'est pas
        en train de jouer, il a donc la valeur x"""
        self.valeur = "x"
