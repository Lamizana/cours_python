class Time(object):
    """
    Definition d'objet temporel.
    Permet d'effectuer une serie d'operations sur des durees.
    """

    def __init__(self, hh = 12, mm = 0, ss = 0):
        self.heure = hh
        self.minute = mm
        self.seconde = ss


    def affiche_heure(self) -> None:
        """Affiche l'heure."""
        print(f"{self.heure}:{self.minute}:{self.seconde}")


#####################################################################
def main() -> int:
    """
    Programme principal.
    """

    # Declare une instance et lui assigne des valeurs :
    instant = Time()
    instant.heure = 11
    instant.minute = 34
    instant.seconde = 25
    instant.affiche_heure()

    t_start = Time()
    t_start.affiche_heure()

    # Creation et initialisation simultanees d un nouvel objet :
    recreation = Time(10, 15, 24)
    recreation.affiche_heure()

    rentree = Time(10, 30)
    rentree.affiche_heure()

    rendez_vous = Time(hh = 18)
    rendez_vous.affiche_heure()

    return (0)


#####################################################################
if __name__ == "__main__":
    main()
