#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################


class Domino(object):
    """
    Classe simulant les pieces d un jeu de Domino.
    """

    def __init__(self, a = 0, b = 0):
        self.face_a = a
        self.face_b = b


    def affiche_point(self) -> None:
        """Affiche les points present sur chaque face."""
        print(f"- Face A : {self.face_a}\t- Face B : {self.face_b}")


    def valeur(self) -> int:
        """Renvoie la somme des points des 2 faces."""
        somme = self.face_a + self.face_b
        return (somme)


#####################################################################
def main() -> int:
    """
    Programme principal.
    """

    d1 = Domino(2, 6)
    d2 = Domino(4, 3)

    d1.affiche_point()
    d2.affiche_point()

    print(f"Total des points : {d1.valeur() + d2.valeur()}")

    # Creation d'une liste de dominos :
    dominos = []
    for i in range(7):
        dominos.append(Domino(6, i))
        dominos[i].affiche_point()

    return (0)


#####################################################################
if __name__ == "__main__":
    main()
