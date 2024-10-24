#######################################################################
"""
Transformez vos données en tableaux

Pour cette seconde tâche, nous travaillons toujours sur les mêmes 10 clients, 
mais nous avons cette fois trois informations à disposition sur chacun d’eux :

    le revenu mensuel
    l'âge du client
    le nombre d’enfants à charge

L’objectif va être de créer un tableau NumPy à partir de ces informations et 
de répondre aux différentes demandes formulées par notre service prêt en 
manipulant ce tableau  techniques.
"""
#######################################################################
import numpy as np
#######################################################################

def create_array(liste: list) -> np.array:
    """Creer un array a partir d'une liste"""

    data = np.array(liste)
    return (data)

# ---------------------------------------------------------------------
def display_client(data: np.array, index: int) -> None:
    """Affiche les informations de Paul qui lui sont relatives ainsi
    que sont taux de remboursement mensuel (35%)"""

    print("\n- Les informations de Paul: ", data[index, :])

    max_remb = round(data[index, 0] * 0.35, 1)
    print("\tLe remboursement max de Paul est de ", max_remb)
    return


# ---------------------------------------------------------------------
def main() -> int:
    """Fonction principal"""

    hugo = [1800, 21, 0]
    richard = [1500, 54, 2]
    emilie = [2200, 28, 3]
    pierre = [3000, 37, 1]
    paul = [2172, 37, 2]
    deborah = [5000, 32, 0]
    yohann = [1400, 23, 0]
    anne = [1200, 25, 1]
    thibault = [1100, 19, 0]
    emmanuel = [1300, 31, 2]

    tableau = [hugo, richard, emilie, pierre, paul, deborah,
            yohann, anne, thibault, emmanuel]
    print("- Liste: ", tableau)

    data = create_array(tableau)
    print("- Array:\n", data)

    display_client(data, 4)

    # Rajoute un client a data :
    louise = [1900, 31, 1]
    np.vstack((data, louise))
    print("\n- New Array:\n", data)

    # Stockez enfin l'ensemble des informations de salaire de notre clientèle 
    # dans une variable revenus :
    revenus = data[:, 0]
    print("\n- Voici les revenues de chaque client:", revenus)

    return (0)


#######################################################################
if __name__ == "__main__":
    main()