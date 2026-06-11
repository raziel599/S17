"""Diagnostic d'ouverture - soirée 17 (à exécuter, puis à analyser).

Ce programme prépare un catalogue, y ajoute un livre, puis construit
l'ensemble des livres « distincts » pour les compter. Le compte affiché
n'est pas celui que l'on attend, et un livre a disparu de la liste.

Votre travail (avant d'écrire la moindre correction) :
  1. Exécutez ce fichier et lisez ce qu'il affiche.
  2. Recopiez le compte obtenu et la liste des titres affichés.
  3. Formulez une hypothèse : pourquoi deux livres aux titres
     différents sont-ils comptés comme un seul ? Qu'est-ce qui, pour
     un ensemble, rend deux livres « identiques » ?

Ne corrigez rien tant que le diagnostic n'est pas écrit.

Fichier distribué aux étudiants.

Programmation Orientée Objet - EICPN 2025-2026.
"""

from livre_s17 import Livre


if __name__ == "__main__":
    catalogue = [
        Livre("1984", "Orwell", "9780451524935", 328, 1949),
        Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
        Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
    ]

    # On reçoit une réédition, avec un nouveau titre de couverture.
    reedition = Livre("1984 (édition collector)", "Orwell",
                      "9780451524935", 328, 1949)

    tous = catalogue + [reedition]
    print(f"Livres ajoutés au catalogue : {len(tous)}")

    distincts = set(tous)
    print(f"Livres distincts (set)      : {len(distincts)}")
    print("Titres conservés :")
    for livre in distincts:
        print(f"  - {livre.titre}")
