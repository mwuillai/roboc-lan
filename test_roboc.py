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

class TestLabyrinthe:
    carte_longueur, carte_test = (carte("cartes","test"))
    lab = Labyrinthe(carte_longueur, carte_test)
    
    def test_labyrinthe(self):
        assert self.carte_longueur == 6
        assert self.lab.cases.values == "O"
