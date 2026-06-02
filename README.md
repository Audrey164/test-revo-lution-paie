# Système de Gestion - REVO-LUTION Paie

Application de gestion du personnel développée en Python avec Tkinter et SQLite. Cette application permet une visualisation dynamique des employés, inclut un moteur de recherche multi-critères et une fonction d'export CSV optimisée pour Excel.

## Prérequis
- Python 3.11 ou version supérieure.
- Aucun module externe n'est requis (utilisation de la bibliothèque standard uniquement).

## Installation et lancement
1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous que le fichier `employees.db` est présent dans le dossier racine du projet.
3. Ouvrez un terminal dans le dossier du projet.
4. Lancez l'application avec la commande suivante :
   ```bash
   python main.py

## Fonctionnalités implémentées
- **Interface graphique** : Utilisation de `Tkinter` pour une interface moderne et redimensionnable.
- **Lecture SQLite** : Chargement fluide des données depuis `employees.db` avec gestion par `Treeview`.
- **Recherche temps réel** : Filtrage multi-critères (Nom, Prénom, Poste, Département).
- **Export CSV** : Exportation des données filtrées vers un fichier CSV avec encodage `utf-8-sig` (compatible Excel) et délimiteur point-virgule.
- **Sécurité** : Utilisation stricte de paramètres préparés (placeholders `?`) dans les requêtes SQL pour prévenir toute injection.

## Capture d'écran
<img width="1917" height="1020" alt="Capture1" src="https://github.com/user-attachments/assets/f3aa4216-fc33-47e7-a595-fe06db5d621e" />
<img width="1917" height="1015" alt="Capture2" src="https://github.com/user-attachments/assets/090ad6b5-24df-4b2d-b284-752036cdfc1d" />
<img width="1917" height="1018" alt="Capture3" src="https://github.com/user-attachments/assets/b825c8f1-4849-435b-b2b5-3f1cbe43ba00" />
<img width="1916" height="1022" alt="Capture4" src="https://github.com/user-attachments/assets/9cb7bd93-7bf6-4670-9c06-8a2b771f8c40" />

