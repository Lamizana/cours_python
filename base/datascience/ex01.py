#######################################################################
"""
Nous avons à notre disposition les revenus de 10 clients de notre banque. 
Utiliser les différentes manipulations présentées dans ce chapitre 
pour sélectionner certains revenus selon une condition spécifique et 
effectuer diverses opérations.
"""
#######################################################################
import numpy as np

def transform_list(liste: list) -> np.array:
    """Transforme une liste en array"""

    array = np.array(liste)
    return (array)


def high_revenue(array: np.array) -> np.array:
    """créez un nouvel array haut_revenus dans lequel vous sélectionnerez 
    l'ensemble des revenus supérieurs ou égal à 3000€ :"""

    haut_revenue = array[array >= 3000]
    return (haut_revenue)


def annual_revenue(revenue: np.array) -> float:
    """calculez dans un premier temps la somme des revenus annuelle.
    Pour rappel, les revenus listés ci dessus sont mensuels."""

    revenue_mensuel = revenue.sum()
    revenue_annuel = revenue_mensuel * 12

    return (revenue_annuel)

def moyenne_revenue(array: np.array) -> float:
    """calculez la moyenne des revenus des 10 clients"""

    moyenne = array.mean()
    return (moyenne)


def main() -> int:
    """Fonction programme principal"""

liste = [1800, 1500, 2200, 3000, 2172, 5000, 1400, 1200, 1100, 1300]

array = transform_list(liste)
print(f"- Valeurs de l'array: {array}")

haut_revenue = high_revenue(array)
print(f"- Les revenues superieur a 3000 euros: {haut_revenue}")

revenue_annuel = annual_revenue(array)
print(f"- La somme des revenues annuels: {revenue_annuel}")

moyenne = moyenne_revenue(array)
print(f"- La moyenne des revenues mensuel des 10 clients: {moyenne}")

# Augmente de 200 le client avec un revenue a 1400 :
array[array == 1400] = 1600
print(array)


#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    main()