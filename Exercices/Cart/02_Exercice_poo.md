### Exercice 2 : Création d'une classe `Product` et d'un `Storage` utilisant un dictionnaire

#### Développez :

- Reprenez l'exercice précédent en créeant un CartService dans un dossier Services à la racine du projet. Et commandez des produits dans le fichier app.py

```txt
Cart/
│
├── app/               # Code source
│   └── Services/      # Code lié aux technologies sous-jacentes (bases de données, API, etc.)
│
└── app.py             # Point d'entrée de l'application
```

Voici ce que vous devriez implémenter dans la classe `CartService`

```python
# Classe principale du service panier
class CartService:
    def __init__(self, storage):
        pass

    def buy(self, product, quantity: int) -> None:
        pass

    def total(self) -> float:
        pass

    def reset_command(self) -> None:
        pass

    def restore_command(self, name: str) -> None:
        pass
```


- Dans le fichier app.py

```python
from Services.CartService import CartService
from typing import List, Dict

# Classe Product
class Product:
    def __init__(self, name: str, price: float):
        """
        Constructeur pour initialiser le produit avec son nom et son prix.
        """
        self.name = name
        self.price = price

# Classe Storage
class DictStorage():
    pass

# Création des produits
laptop = Product("Laptop", 2400.0)
mouse = Product("Mouse", 75.0)
keyboard = Product("Keyboard", 50.0)

# Initialisation du stockage
storage = DictStorage()

# Ajout des produits dans le stockage
storage.set_value(laptop.name, laptop.price)
storage.set_value(mouse.name, mouse.price)
storage.set_value(keyboard.name,keyboard.price)

cart = CartService(storage)

# Total
print(f"Total : {cart.total()} €")

# Retirer un produit du panier 
cart.restore_command('Laptop')
print(f"Total : {cart.total()} €")

# Retirez tous les produits du panier 
cart.reset_command()
print(f"Total : {cart.total()} €")
```