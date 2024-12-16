### Exercice 2 : Création d'une classe `Product` et d'un `Storage` utilisant un dictionnaire

#### Développez :

- Refactorez le projet comme suit, puis testez le dans le fichier app.py

```txt
└── app
    ├── Domain
    │   ├── Models
    │   │   └── Product.py        # Contient la classe Product
    │   ├── Services
    │   │   └── CartService.py    # Contient la classe CartService
    │   └── __init__.py           # Initialisation du module Domain
    ├── Infrastructures
    │   ├── DictStorage.py        # Contient la classe DictStorage
    │   └── __init__.py           # Initialisation du module Infrastructures
    ├── app.py                    # Fichier principal pour démarrer l'application
    └── requirements.txt          # Liste des dépendances du projet

```


