# Programmation orientée objet - Soirée 17

## Structures de données objet

Dépôt de l'atelier de la soirée 17. Il porte sur les **structures de données objet** : tris avec `sorted(key=...)`, recherches, et collections d'objets (`set`, `dict`), appliqués à un catalogue de `Livre`.

L'énoncé complet et les consignes détaillées se trouvent dans **`POO_S17_atelier_TP.pdf`**. Lisez-le en premier : c'est la référence unique pour les spécifications (valeurs, formats, comportements attendus).

> Vous travaillerez dans **VS Code**. Toutes les actions Git peuvent se faire à la souris depuis le panneau **Contrôle de code source** ; les commandes en ligne de commande sont rappelées en complément.

---

## 1. Ce que contient ce dépôt

| Fichier | Rôle |
|---|---|
| `POO_S17_atelier_TP.pdf` | L'énoncé. Référence unique des consignes. |
| `livre_s17.py` | La classe `Livre` (lecture seule). Ne pas la modifier. |
| `catalogue_squelette.py` | Le squelette à compléter. **Renommez-le en `catalogue.py`.** |
| `tri_buggy.py` | Le programme de l'exercice 1 (diagnostic). À exécuter, pas à corriger. |
| `reponses.txt` | Gabarit pour vos réponses écrites (exercices 1, 3 et 5). |

## 2. Ce que vous devez produire

À déposer dans votre fork :

- `catalogue.py` — le squelette complété (exercices 2 à 6) ;
- `test_catalogue.py` — votre suite de tests `unittest` (exercice 7) ;
- `reponses.txt` — vos réponses écrites (exercices 1, 3 et 5).

> Ne modifiez pas `livre_s17.py`. Toutes vos fonctions reçoivent une liste de `Livre` et n'ont pas le droit de la modifier : produisez toujours une nouvelle collection.

---

## 3. Mise en route (dans VS Code)

1. **Forkez** ce dépôt depuis GitHub (bouton **Fork** en haut à droite). Vous obtenez votre copie : `https://github.com/VOTRE-PSEUDO/S17`.
2. **Clonez votre fork** dans VS Code : ouvrez la palette de commandes (`Ctrl+Shift+P`), tapez **`Git: Clone`**, collez l'URL de **votre** fork, choisissez un dossier.
3. **Renommez le squelette** : clic droit sur `catalogue_squelette.py` → **Renommer** → `catalogue.py`.

*Équivalents terminal :*

```bash
git clone https://github.com/VOTRE-PSEUDO/S17.git
cd S17
git mv catalogue_squelette.py catalogue.py
```

---

## 4. Committer votre travail au fil des exercices

1. Ouvrez le panneau **Contrôle de code source** (icône en forme de branches, ou `Ctrl+Shift+G`).
2. Vos fichiers modifiés apparaissent sous **Modifications**.
3. Cliquez sur le **`+`** d'un fichier pour l'indexer, ou sur le `+` de la section pour tout indexer.
4. Écrivez un **message de commit** clair dans la zone en haut.
5. Cliquez sur **Valider** (la coche `✓`, ou `Ctrl+Entrée`).

*Équivalent terminal :*

```bash
git add catalogue.py
git commit -m "Exercice 2 : tris par sorted(key=...)"
```

### Cadence de commits conseillée

Un commit par exercice. Des commits petits et réguliers facilitent le suivi et le feedback.

| Après l'exercice | Fichier(s) | Message de commit suggéré |
|---|---|---|
| 1 | `reponses.txt` | `Exercice 1 : diagnostic du set` |
| 2 | `catalogue.py` | `Exercice 2 : tris par sorted(key=...)` |
| 3 | `catalogue.py`, `reponses.txt` | `Exercice 3 : cle composee et justification` |
| 4 | `catalogue.py` | `Exercice 4 : recherches` |
| 5 | `catalogue.py`, `reponses.txt` | `Exercice 5 : dedoublonnage et justification` |
| 6 | `catalogue.py` | `Exercice 6 : index et regroupement` |
| 7 | `test_catalogue.py` | `Exercice 7 : tests unittest` |

---

## 5. Pousser vers votre fork (dans VS Code)

Après un ou plusieurs commits, cliquez sur **Synchroniser les modifications** dans le panneau Contrôle de code source (ou sur l'icône de synchronisation en bas à gauche). Vos commits partent vers votre fork en ligne.

*Équivalent terminal :* `git push`

Vérifiez sur la page de votre fork (`https://github.com/VOTRE-PSEUDO/S17`) que vos fichiers et vos commits y apparaissent.

---

## 6. Remise par pull request (sur le site GitHub)

La remise se fait par **pull request** depuis votre fork vers le dépôt du cours.

1. Sur la page de votre fork, cliquez sur **« Contribute »** puis **« Open pull request »** (ou sur le bandeau vert **« Compare & pull request »**).
2. Vérifiez **attentivement** la direction :
   - **base repository** : `FabienToune/S17` (le dépôt du cours) — **base** : `main`
   - **head repository** : `VOTRE-PSEUDO/S17` (votre fork) — **compare** : `main`
3. Titre suggéré : `Rendu atelier S17 - Prenom NOM`. Décrivez ce que vous avez fait et vos éventuelles questions.
4. Cliquez sur **« Create pull request »**.

> **Important :** votre pull request **ne sera pas fusionnée**, et c'est normal. Elle sert de **point de remise** (daté, traçable) et d'**espace de feedback**, où l'enseignant commentera votre code. Ne la fermez pas et ne la fusionnez pas vous-même.

Assurez-vous d'avoir **synchronisé** votre dernier commit avant la date de remise.

---

## En cas de blocage

Relisez d'abord l'énoncé (`POO_S17_atelier_TP.pdf`), puis sollicitez l'enseignant. Coder un énoncé mal lu coûte plus cher que relire l'énoncé.

---

*EICPN - Enseignement pour Adultes. Programmation orientée objet (UAA 7525 21 U32 D3).*
