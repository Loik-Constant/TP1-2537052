# Travail Pratique 1 : Gestionnaire de Mots de Passe

**Objectif :** Mettre en œuvre les concepts de programmation orientée objet (POO) en Python, la gestion de la ligne de
commande (CLI) et le développement d'interfaces graphiques avec la bibliothèque **PySide6**.

**Modalités :**

- **Travail individuel.**
- **L'utilisation de l'IA est strictement interdite.**
- **Dates limites :**
    - Partie 1 : **6 octobre** avant minuit.
    - Partie 2 : **27 octobre** avant minuit.

---

## Modalités de Remise et Structure du Projet

Votre travail doit être soumis via un dépôt **Git sur GitHub** partagé avec l'utilisateur **profdenis**. Une attention
particulière sera portée à la structure du projet, à la gestion des dépendances et à la rigueur de l'historique Git.

### 1. Gestion des dépendances avec `uv`

L'utilisation de l'outil **`uv`** est obligatoire pour la gestion de l'environnement virtuel et des dépendances.

- Vous devez inclure les fichiers de configuration générés par `uv` (`pyproject.toml` et `uv.lock`).
- **Important :** Vous devez configurer un fichier `.gitignore` rigoureux. **Ne commitez jamais** le dossier de
  l'environnement virtuel (ex: `.venv/`), les fichiers de cache Python (`__pycache__/`) ou les fichiers de données
  sensibles (comme le fichier `vault.json`).

### 2. Structure des fichiers

Votre dépôt doit respecter une architecture modulaire :

```text
votre-projet/
├── .gitignore
├── pyproject.toml
├── uv.lock
├── main.py                 # Point d'entrée unique (gère les modes CLI ou UI)
├── README.md               # Description et instructions de lancement
├── doc/                    # Maquettes (PDF ou images)
└── app/                    # Package principal de l'application
    ├── __init__.py
    ├── core/               # LOGIQUE MÉTIER (Partie 1)
    │   ├── __init__.py
    │   ├── generator.py    # Logique de génération de mots de passe
    │   └── storage.py      # (Nouveau) Gestion du fichier JSON simple
    └── ui/                 # INTERFACE GRAPHIQUE (Partie 2)
        ├── __init__.py
        ├── main_window.py  # Fenêtre principale (Coffre-fort)
        └── generator_ui.py # Fenêtre/Dialogue de génération
```

* **En Partie 1 :** Votre dossier `app/` ne contiendra que le sous-dossier `core/`.
* **En Partie 2 :** Vous ajouterez le sous-dossier `ui/` à l'intérieur de `app/`.
* **Note importante :** Chaque fichier `.py` doit débuter par un commentaire contenant le nom, le numéro d'étudiant et
  le nom d'utilisateur GitHub de chaque membre de l'équipe.

### 3. Stratégie de branches et historique Git

Vous devez fournir deux branches distinctes :

* **Branche `partie1` :**
    * Contient uniquement la logique de la **Partie 1** (`app/core/`), le fichier `main.py` (configuré pour le mode CLI)
      et le dossier `doc/`.
    * Le **dernier commit** de cette branche doit impérativement avoir lieu **avant la date limite de la Partie 1**.

* **Branche `partie2` :**
    * Contient l'intégralité du projet (Partie 1 **ET** Partie 2 complétée).
    * Le **dernier commit** de cette branche doit impérativement avoir lieu **avant la date limite de la Partie 2**.

**Règles d'utilisation de Git :**

- **Commits fréquents :** Réalisez des commits réguliers avec des messages explicites.
- **Qualité du dépôt :** Un dépôt contenant un seul commit massif le jour de la remise sera lourdement pénalisé.
  L'historique des commits est un élément essentiel de l'évaluation.

---

## Partie 1 : Logique Métier et Interface en Ligne de Commande (CLI)

L'objectif est de concevoir un moteur de génération de mots de passe fonctionnel et testable en ligne de commande.

### 1. Logique de génération (Back-end)

Vous devez créer une classe `PasswordGenerator` qui supporte :

- La définition de la **longueur** du mot de passe.
- La sélection des **types de caractères** (minuscules, majuscules, chiffres, symboles).
- L'option de **validation** : si activée, le mot de passe doit contenir au moins un caractère de chaque type
  sélectionné.

### 2. Interface en ligne de commande (CLI)

Votre programme, via `main.py`, doit accepter les arguments suivants :

- `--length` (int) : définit la longueur (par défaut 16).
- Options d'exclusion : `--no-lower`, `--no-upper`, `--no-digits`, `--no-symbols`.
- `--validate` : active la validation obligatoire.

### 3. Maquettes (Design)

Vous devez fournir des **maquettes (dessins ou fichiers numériques)** de l'interface finale :

- Une vue de la fenêtre de génération de mot de passe.
- Une vue de la fenêtre principale du "Coffre-fort" (liste des entrées, boutons de gestion).

**Livrables Partie 1 :**

- Le code source Python (logique métier dans `core/` et interface CLI dans `main.py`).
- Le fichier README.md contenant vos maquettes (images insérées dans le fichier Markdown.

---

## Partie 2 : Interface Graphique avec PySide6

L'objectif est de transformer la logique de la Partie 1 en une application complète avec une interface utilisateur (UI)
ergonomique.

### 1. Le Générateur de Mots de Passe (Fenêtre/Dialogue)

L'interface doit permettre de :

- Choisir la longueur via un **slider** (curseur) et des boutons incrémentaux.
- Sélectionner les types de caractères via des **checkboxes**.
- Afficher le mot de passe dans un label large et sélectionnable.
- Masquer/Afficher le mot de passe (affichage sous forme d'astérisques `****` ou texte clair).
- Copier le mot de passe dans le presse-papiers via un bouton "Copier".

### 2. Le Coffre-fort (Fenêtre Principale)

Cette fenêtre gère une collection de couples (e-mail / mot de passe) :

- **Affichage :** Une liste défilante (`QScrollArea`) affichant les e-mails. Les mots de passe doivent être masqués
  (`*******`) par défaut.
- **Interaction :** Un double-clic ou un menu contextuel (clic droit) doit permettre de révéler temporairement le mot de
  passe.
- **Tri :** Possibilité de trier la liste par e-mail (ordre alphabétique).
- **Gestion des entrées (CRUD) :**
    - **Ajouter :** Ouvrir une boîte de dialogue (e-mail et mot de passe). Le bouton "Générer" de cette boîte doit
      lancer la logique de la Partie 1.
    - **Modifier :** Modifier une entrée existante.
    - **Supprimer :** Retirer une entrée après confirmation.
- **Persistance :** Les données doivent être sauvegardées dans un fichier **`vault.json`** (format texte clair) lors de
  la fermeture de l'application et chargées au démarrage.

### 3. Intégration et Modes d'exécution

L'interface doit être réactive (utilisation de `QVBoxLayout`, `QHBoxLayout`, etc.) et gérer les erreurs de manière
élégante (ex: fichier corrompu).

**Contraintes de `main.py` :**
Vous devez implémenter une gestion d'arguments permettant de basculer entre les deux modes :

- **Mode CLI :** L'argument `--no-gui` permet d'exécuter uniquement la logique de la Partie 1 en ligne de commande.
- **Mode GUI (par défaut) :** L'application lance l'interface graphique.

- **Mode CLI :** L'argument `--no-gui` permet d'exécuter uniquement la logique de la Partie 1.
- **Mode GUI (par défaut) :** L'application lance l'interface graphique.
- **Argument `--vault_file` :** Permet de spécifier un fichier JSON personnalisé (sinon, utilisation de
  `vault.json` par défaut). 

---

## Critères de Notation

| Critère               | Description                                                                   |
|:----------------------|:------------------------------------------------------------------------------|
| **Fonctionnalité**    | Toutes les fonctions (CLI, GUI, CRUD, Copie, Masquage) fonctionnent.          |
| **Qualité de la POO** | Code modulaire, classes bien définies, séparation logique/UI respectée.       |
| **Interface (UI/UX)** | Utilisation correcte de PySide6, ergonomie, cohérence visuelle.               |
| **Robustesse**        | Gestion des erreurs (fichiers, entrées utilisateur) et intégrité des données. |
| **Documentation**     | Code commenté et README clair.                                                |

---

**Bonus (Optionnel - Niveau Expert) :**

- **Sécurité :** Au lieu d'un fichier JSON en clair, implémentez un chiffrement réel des données (utilisez le module
  `cryptography` et le fichier `vault.py` fourni en annexe).
- **Recherche :** Ajouter une barre de filtrage pour les e-mails.
- **Force :** Ajouter un indicateur de force du mot de passe (couleur dynamique).
- Système de catégories pour les entrées.
