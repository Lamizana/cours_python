#####################################################################
class Mammifere(object):
    """
    Contient un ensemble de caracteristiques propre aux mammiferes.
    """

    caract_1 = "Il allaite ses petits."


# ----------------------------------------------------------------- #
class Carnivore(Mammifere):
    """
    Herite de la classe mammifere et lui rajoute des specificitees.
    """

    caract_2 = "Il se nourrit de la chaire de ses proies."


# ----------------------------------------------------------------- #
class Chien(Carnivore):
    """
    Herite de la classe Carnivore qui herite elle-meme de Mammifere.
    """

    caract_3 = "Son cri est l'aboiement."


#####################################################################
def main() -> int:
    """
    Programme principal.
    """

    ector = Chien()
    print(ector.caract_1, ector.caract_2, ector.caract_3)

    return (0)


#####################################################################
if __name__ == "__main__":
    main()