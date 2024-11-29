#####################################################################
from math import sqrt

class Point(object):
    """
    Definition d'un point geometrique.
    """

# ----------------------------------------------------------------- #
def affiche_point(p: Point) -> None:
    """
    Affiche les points de l'objet.
    """

    print(f"- Coord. horizontale: {p.x}\n- Coord. vertical: {p.y}")


# ----------------------------------------------------------------- #
def distance(p1: Point, p2: Point) -> float:
    """
    Calcul la distance entre 2 points avec Pythagore.
    """

    dist_x = abs(p1.x - p2.x)
    dist_y = abs(p1.y - p2.y)

    value = sqrt(dist_x * dist_x + dist_y * dist_y)
    return (value)


# ----------------------------------------------------------------- #
def main() -> int:
    """
    Programme principal.
    """

    # Creation d une instance Point() :
    p9 = Point()
    print(p9.__doc__)
    print("Type et Adresse: ", p9, "\n")

    # Assignation des valeurs dans cette instance :
    p9.x = 3.0
    p9.y = 4.0

    # Definition des 2 Points et calcul leur distance :
    p1, p2 = Point(), Point()
    p1.x, p1.y = 10.0, 5.0
    p2.x, p2.y = 3.0, 7

    affiche_point(p1)
    affiche_point(p2)
    print("Distance = ", distance(p1, p2))

    return(0)


#####################################################################
if __name__ == "__main__":
    main()