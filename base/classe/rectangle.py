class Point(object):
    """
    Definition d'un point geometrique.
    """


# ----------------------------------------------------------------- #
class Rectangle(object):
    """
    Définition d'ue classe rectangle.
    """


# ----------------------------------------------------------------- #
def trouve_centre(box: Rectangle) -> Point:
    """
    Trouve le centre d'une boite et retourne ses coordonnees.
    """

    p = Point()
    p.x = box.coin.x + box.largeur / 2.0
    p.y = box.coin.y + box.hauteur / 2.0

    return (p)


#####################################################################
def main() -> None:
    """
    Programme principal.
    """

    # Definit les dimensions du rectangle :
    boite = Rectangle()
    boite.largeur = 50.0
    boite.hauteur = 35.0

    # Definit le coin superieur gauche :
    boite.coin = Point()
    boite.coin.x = 12.0
    boite.coin.y = 27.0

    centre = trouve_centre(boite)
    print(f"- Centre X = {centre.x}")
    print(f"- Centre Y = {centre.y}")
    return (0)


#####################################################################
if __name__ == "__main__":
    main()