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

<img width="1918" height="1026" alt="Capture1" src="https://github.com/user-attachments/assets/d7ba9803-5014-4bea-858c-3a5e11a94b58" />
<img width="1917" height="1013" alt="Capture2" src="https://github.com/user-attachments/assets/0d9b3278-523e-40db-970f-f7d5c248772a" />
<img width="1918" height="1022" alt="Capture3" src="https://github.com/user-attachments/assets/4a301356-dd9d-4ecb-be79-bd12d7556bff" />



<img width="1918" height="1026" alt="Capture1" src="https://github.com/user-attachments/assets/d5bdcc65-76e8-4e8d-b13c-ac6ad50cffa8" />
