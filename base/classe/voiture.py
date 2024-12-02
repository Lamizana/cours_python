#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################


class Voiture(object):
    """
    Instancie des objets reproduisant le comportement de voiture.
    """

    def __init__(self, marque = 'Ford', couleur = 'rouge'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = 'personne'
        self.vitesse = 0


    def choix_conducteur(self, nom: str) -> None:
        """Change le nom du pilote."""
        self.pilote = nom


    def accelerer(self, taux: float, duree: int) -> None:
        """Fait varier la vitesse du vehicule, acceleration = taux * duree."""
        if self.pilote == 'personne':
            print("Cette voiture n'as pas de conducteur.")
        else:
            self.vitesse = self.vitesse + (taux * duree)


    def affiche_tout(self) -> None:
        """Affiche toutes les informations."""
        print(f"{self.marque} {self.couleur} pilotée par {self.pilote},", end=' ')
        print(f"vitesse = {self.vitesse} m/s")


#####################################################################
def main() -> int:
    """
    Programme principal.
    """

    # Instancie 3 voitures differentes :
    v1 = Voiture(couleur = 'verte')
    v2 = Voiture('Peugeot', 'bleue')
    v3 = Voiture('Mercedes')

    # Changement de conducteur sur v1 et v2:
    v1.choix_conducteur('Harry')
    v2.choix_conducteur('Celine')

    # Change les vitesses :
    v2.accelerer(1.8, 12)
    v3.accelerer(1.9, 11)

    # Affiche les informations :
    v1.affiche_tout()
    v2.affiche_tout()
    v3.affiche_tout()
    
    return (0)


#####################################################################
if __name__ == "__main__":
    main()