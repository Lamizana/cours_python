class CompteBancaire(object):
    """
    Permet d'instancier differents comptes.
    Contient le nom du client et la somme sur son compte.
    """

    def __init__(self, nom = "Dupont", somme = 1000):
        self.nom = nom
        self.somme = somme


    def depot(self, argent: int) -> None:
        """Ajoute une somme au solde."""
        self.somme += argent


    def retrait(self, argent: int) -> None:
        """Retire une somme du solde."""
        self.somme -= argent
    

    def affiche(self) -> None:
        """Affiche le nom du client et son compte."""
        print(f"Le solde du compte bancaire de {self.nom} est de {self.somme} euros.")


#####################################################################
def main() -> int:
    """
    Programme principal.
    """

    compte1 = CompteBancaire('Dushmol', 800)
    compte1.affiche()

    compte1.depot(350)
    compte1.affiche()

    compte1.retrait(200)
    compte1.affiche()

    compte2 = CompteBancaire()
    compte2.depot(25)
    compte2.affiche()

    return (0)


#####################################################################
if __name__ == "__main__":
    main()