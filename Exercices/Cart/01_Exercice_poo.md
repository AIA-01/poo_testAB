### Exercice 1 : Création d'une classe `Product` et d'un `Storage` utilisant un dictionnaire

#### Développez :
- Créer une classe `Product` pour représenter un produit avec un nom et un prix.
- Créer une classe `DictStorage` pour stocker les produits et leurs prix dans un dictionnaire.
  - Si un produit est déjà dans le storage, incrémentez le prix de ce produit.
- Faites les calculs qui se trouvent dans la partie commentaire. 
  
#### Code de l'exercice :

```python
from typing import List, Dict

# Classe Product
class Product:
   pass

# Classe DictStorage
class DictStorage:
    def __init__(self):
        """
        Constructeur pour initialiser le dictionnaire de stockage.
        """
        pass

    def set_value(self, key: str, value: float) -> None:
        """
        Ajoute une nouvelle clé-valeur dans le stockage.
        Lève une exception si la clé existe déjà.
        :param key: La clé à ajouter.
        :param value: La valeur associée.
        """
        pass

    def all(self) -> List[Dict[str, float]]:
        """
        Retourne tous les produits dans le stockage sous forme de liste de tuples (clé, valeur).
        """
        pass

    def reset(self) -> None:
        """
        Réinitialise le stockage en supprimant tous les produits.
        """
        pass

    def restore(self, key: str) -> None:
        """
        Supprime un produit du stockage en fonction de son nom.
        :param key: Le nom du produit à supprimer.
        """
        pass


# Création des produits
laptop = Product("Laptop", 2400.0)
mouse = Product(name = "Mouse", price = 75.0)
keyboard = Product("Keyboard", 50.0)

# Initialisation du stockage
storage = DictStorage()

# Ajout des produits dans le stockage
storage.set_value(laptop.name, laptop.price)
storage.set_value(mouse.name, mouse.price)
storage.set_value(keyboard.name, keyboard.price)

# Affichage de tous les produits du stockage

# Affichage du prix d'un produit spécifique

# Affichage du total des prix 
```
