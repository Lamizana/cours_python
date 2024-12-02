#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################


class Satellite(object):
    """
    Instancie des objets simulant des satellites artificiels
    lance dans l'espace, autour de la Terre.
    """

    def __init__(self, nom: str, masse = 100, vitesse = 0):
        self.nom = nom
        self.masse = masse
        self.vitesse = vitesse


    def affiche_vitesse(self) -> None:
        """Affiche le nom du satelitte et sa vitesse."""
        print(f"Vitesse du satellite {self.nom} = {self.vitesse} m/s.")


    def impulsion(self, force: int, duree: int) -> None:
        """Fait varier la vitesse du satellite."""
        variation = (force * duree) / self.masse
        self.vitesse += variation


    def energie(self) -> int:
        """Renvoie la valeur de l'energie cinetique du satellite."""
        e = (self.masse * (self.vitesse * self.vitesse)) / 2

        return (int(e))


#####################################################################
def main() -> int:
    """
    Progamme principal.
    """

    s1 = Satellite('Zoé', masse = 250, vitesse = 10)

    s1.impulsion(500, 15)
    s1.affiche_vitesse()
    print("Energie:", s1.energie())

    s1.impulsion(500, 15)
    s1.affiche_vitesse()
    print("Nouvelle energie:", s1.energie())

    return (0)


#####################################################################
if __name__ == "__main__":
    main()