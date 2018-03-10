from case import Cases

from labyrinthe import Labyrinthe

from carte import carte


class TestCases:
    case_test_bloquant = Cases("O")
    case_test_non_bloquant = Cases(" ")

    def test_mouvement_entrant_bloquant(self):
        assert self.case_test_bloquant.mouvement_entrant() is False

    def test_mouvement_entrant_non_bloquant(self):
        assert self.case_test_non_bloquant.mouvement_entrant() is True

    def test_mouvement_sortant(self):
        self.case_test_bloquant.mouvement_sortant()
        assert self.case_test_bloquant.valeur == " "


class TestLabyrinthe:
    carte_longueur, carte_test = (carte("cartes", "test"))
    lab = Labyrinthe(carte_longueur, carte_test)

    def test_labyrinthe(self):
        assert self.carte_longueur == 6
        assert self.lab.cases[(0, 0)].valeur == "o"
        assert self.lab.cases[(1, 1)].valeur == " "
        assert self.lab.cases[(2, 2)].valeur == " "
        assert self.lab.cases[(3, 3)].valeur == " "
        assert self.lab.cases[(4, 4)].valeur == "o"


    def test_placement(self):
        self.lab.placement(1)
        assert self.lab.cases[self.lab.joueurs[0]].valeur == "x"
