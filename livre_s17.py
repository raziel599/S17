"""Classe Livre - brique réutilisée en soirée 17 (structures de données objet).

Reprise inchangée de la classe Livre des soirées 12 à 14. Aucune
modification : la soirée 17 manipule des *collections* de Livre
(listes, ensembles, dictionnaires) sans toucher à la classe.

Deux décisions de conception héritées sont déterminantes pour S17 :

  - Livre n'a NI __lt__ NI @total_ordering. Il n'existe aucun ordre
    naturel : trier impose donc sorted(key=...).
  - Livre possède __eq__ et __hash__ basés sur l'ISBN (identité
    métier). C'est cette identité qui rend possibles le
    dédoublonnage par set et l'indexation par dict.

Fichier distribué aux étudiants - lecture seule.

Programmation Orientée Objet - EICPN 2025-2026.
"""



class Livre:
    """Représente un livre du catalogue de la bibliothèque.

    Un Livre est une ENTITÉ largement immuable : son identité métier
    est son ISBN, et ses cinq caractéristiques (titre, auteur, ISBN,
    nombre de pages, année) sont fixées à la construction et ne
    changent plus. Seule la disponibilité change au cours du temps.

    Attributes:
        titre (str): Titre du livre, lecture seule.
        auteur (str): Nom de l'auteur, lecture seule.
        isbn (str): Code ISBN-13 (13 chiffres exactement), lecture seule.
        nb_pages (int): Nombre de pages (strictement positif), lecture seule.
        annee (int): Année de publication (1455 à 2026), lecture seule.
        disponible (bool): État de disponibilité, lecture seule.
            Modifié uniquement par emprunter() et rendre().
    """

    def __init__(self, titre, auteur, isbn, nb_pages, annee):
        """Initialise un Livre en validant toutes les caractéristiques.

        Args:
            titre (str): Titre du livre, non vide.
            auteur (str): Nom de l'auteur, non vide.
            isbn (str): Code ISBN-13, 13 chiffres exactement.
            nb_pages (int): Nombre de pages, strictement positif.
            annee (int): Année de publication, entre 1455 et 2026.

        Raises:
            TypeError: Si nb_pages ou annee n'est pas un int.
            ValueError: Si une valeur ne satisfait pas les contraintes.
        """
        if not isinstance(titre, str) or not titre.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        if not isinstance(auteur, str) or not auteur.strip():
            raise ValueError("L'auteur ne peut pas être vide.")
        if not Livre.isbn_valide(isbn):
            raise ValueError(
                "ISBN invalide : 13 chiffres exactement attendus."
            )
        if not isinstance(nb_pages, int) or isinstance(nb_pages, bool):
            raise TypeError("Le nombre de pages doit être un entier.")
        if nb_pages <= 0:
            raise ValueError(
                "Le nombre de pages doit être strictement positif."
            )
        if not isinstance(annee, int) or isinstance(annee, bool):
            raise TypeError("L'année doit être un entier.")
        if not 1455 <= annee <= 2026:
            raise ValueError(
                "L'année doit être comprise entre 1455 et 2026."
            )

        self._titre = titre
        self._auteur = auteur
        self._isbn = isbn
        self._nb_pages = nb_pages
        self._annee = annee
        self._disponible = True

    # ------------------------------------------------------------------
    # Properties en lecture seule
    # ------------------------------------------------------------------

    @property
    def titre(self):
        """str: Titre du livre (lecture seule)."""
        return self._titre

    @property
    def auteur(self):
        """str: Nom de l'auteur (lecture seule)."""
        return self._auteur

    @property
    def isbn(self):
        """str: Code ISBN-13 du livre (lecture seule)."""
        return self._isbn

    @property
    def nb_pages(self):
        """int: Nombre de pages du livre (lecture seule)."""
        return self._nb_pages

    @property
    def annee(self):
        """int: Année de publication (lecture seule)."""
        return self._annee

    @property
    def disponible(self):
        """bool: État de disponibilité (lecture seule)."""
        return self._disponible

    # ------------------------------------------------------------------
    # Méthode statique
    # ------------------------------------------------------------------

    @staticmethod
    def isbn_valide(chaine):
        """Vérifie qu'une chaîne est un ISBN-13 de forme valide.

        Args:
            chaine (str): Chaîne à vérifier.

        Returns:
            bool: True si la chaîne contient exactement 13 chiffres.
        """
        if not isinstance(chaine, str):
            return False
        if len(chaine) != 13:
            return False
        return chaine.isdigit()

    # ------------------------------------------------------------------
    # Constructeur alternatif
    # ------------------------------------------------------------------

    @classmethod
    def depuis_chaine_csv(cls, ligne):
        """Crée un Livre à partir d'une ligne CSV.

        Args:
            ligne (str): Ligne au format
                'titre;auteur;isbn;nb_pages;annee'.

        Returns:
            Livre: Un nouveau Livre initialisé avec les valeurs
                extraites.

        Raises:
            ValueError: Si la ligne ne contient pas exactement
                cinq champs séparés par des points-virgules.
        """
        champs = ligne.split(";")
        if len(champs) != 5:
            raise ValueError(
                "La ligne doit contenir exactement 5 champs séparés "
                "par des points-virgules."
            )
        titre, auteur, isbn, nb_pages_txt, annee_txt = champs
        return cls(titre, auteur, isbn, int(nb_pages_txt), int(annee_txt))

    # ------------------------------------------------------------------
    # Méthodes métier
    # ------------------------------------------------------------------

    def emprunter(self):
        """Marque le livre comme emprunté.

        Raises:
            ValueError: Si le livre est déjà emprunté.
        """
        if not self._disponible:
            raise ValueError("Livre déjà emprunté")
        self._disponible = False

    def rendre(self):
        """Marque le livre comme rendu (à nouveau disponible).

        Raises:
            ValueError: Si le livre est déjà disponible.
        """
        if self._disponible:
            raise ValueError("Livre déjà disponible")
        self._disponible = True

    def taille_estimee(self):
        """Retourne une description lisible de la taille du livre.

        Pour un Livre imprimé, l'unité naturelle est la page.
        Cette méthode est destinée à être REDÉFINIE par les
        sous-classes qui ont une unité plus naturelle (format
        de fichier pour un livre numérique, durée pour un livre
        audio).

        Returns:
            str: Description de la forme 'N pages'.
        """
        return f"{self._nb_pages} pages"

    # ------------------------------------------------------------------
    # Représentations
    # ------------------------------------------------------------------

    def __str__(self):
        """Retourne une représentation lisible pour l'utilisateur."""
        etat = "disponible" if self._disponible else "emprunté"
        return (
            f'"{self._titre}" de {self._auteur} ({self._annee}) - '
            f"{self._nb_pages} p. - {etat}"
        )

    def __repr__(self):
        """Retourne une représentation non ambiguë pour le débogage."""
        return (
            f"Livre(titre={self._titre!r}, auteur={self._auteur!r}, "
            f"isbn={self._isbn!r}, nb_pages={self._nb_pages}, "
            f"annee={self._annee})"
        )

    # ------------------------------------------------------------------
    # Méthodes spéciales d'identité
    # ------------------------------------------------------------------

    def __eq__(self, autre):
        """Égalité par ISBN (Livre est une entité)."""
        if not isinstance(autre, Livre):
            return NotImplemented
        return self._isbn == autre._isbn

    def __hash__(self):
        """Hash cohérent avec __eq__ (basé sur l'ISBN)."""
        return hash(self._isbn)


if __name__ == "__main__":
    livre = Livre("1984", "Orwell", "9780451524935", 328, 1949)
    print(livre)
    print(f"taille_estimee() : {livre.taille_estimee()}")
