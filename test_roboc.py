"""Module de test. Pour lancer les tests installer le module
pytest avec pip et lancer les tests avec pytest."""
from case import Cases

from labyrinthe import Labyrinthe

from carte import carte


class TestCases:
    """Test du module cases"""
    case_test_bloquant = Cases("O")
    case_test_non_bloquant = Cases(" ")

    def test_mouvement_entrant_bloquant(self):
        """test du mouvement entrant dans le scenario ou la destination
        est bloquante"""
        assert self.case_test_bloquant.mouvement_entrant() is False

    def test_mvmt_entrant_non_bloquant(self):
        """test dans le cas ou le mouvement est non bloquant"""
        assert self.case_test_non_bloquant.mouvement_entrant() is True

    def test_mvmt_entrant_non_bloquant2(self):
        """test dans le cas ou le mouvement est non bloquant2"""
        self.case_test_non_bloquant.mouvement_entrant()
        assert self.case_test_non_bloquant.valeur == "X"

    def test_mouvement_sortant(self):
        """test du mouvement sortant"""
        self.case_test_bloquant.mouvement_sortant()
        assert self.case_test_bloquant.valeur == " "


class TestLabyrinthe:
    """Test du module labyrinthe"""
    carte_longueur, carte_test = (carte("cartes", "test"))
    lab = Labyrinthe(carte_longueur, carte_test)

    def test_labyrinthe(self):
        """test de la bonne creation du labyrinthe"""
        assert self.carte_longueur == 6
        assert self.lab.cases[(0, 0)].valeur == "o"
        assert self.lab.cases[(1, 1)].valeur == " "
        assert self.lab.cases[(2, 2)].valeur == " "
        assert self.lab.cases[(3, 3)].valeur == " "
        assert self.lab.cases[(4, 4)].valeur == "o"

    def test_placement(self):
        """test de la methode de placement"""
        self.lab.placement(1)
        assert self.lab.cases[self.lab.joueurs[0]].valeur == "x"
