from typing import Dict

"""
Séparer dans des fichiers différents, un fichier par classe : Product.py et DictStorage.py

Une classe un role spécifique pour mélanger le code dans une classe 

Architecture, est ce que l'on fait ici du MVC ou autrement ? 
"""

class Product:
    def __init__(self, name: str, price : float):
        self.name = name
        self.price = price
        
class DictStorage:
    
    def __init__(self):
        self.storage : Dict[str, float] = {}
        
    def set_value(self, key: str, value: float) -> None:
        """
        Ajoute une nouvelle clé-valeur dans le stockage.
        Lève une exception si la clé existe déjà.
        :param key: La clé à ajouter.
        :param value: La valeur associée.
        """
        if key in self.storage : 
            self.storage[key] += value
            
            return
        
        self.storage[key] = value

    def all(self) -> Dict[str, float]:
        """
        Retourne tous les produits dans le stockage sous forme de liste de tuples (clé, valeur).
        """
        return self.storage

    def reset(self) -> None:
        """
        Réinitialise le stockage en supprimant tous les produits.
        """
        self.storage.clear()

    def restore(self, key: str) -> None:
        """
        Supprime un produit du stockage en fonction de son nom.
        :param key: Le nom du produit à supprimer.
        """
        if key in self.storage:
            del self.storage[key]
            
    def get_value(self, key : str) -> float:
        
        if key not in self.storage:
            raise ValueError(f"Le produit {key} n'existe pas dans le storage")
        
        return self.storage[key]
    

# Création des produits
laptop = Product("Laptop", 2400.0)
mouse = Product("Mouse", 75.0)
keyboard = Product("Keyboard", 50.0)

# Initialisation du stockage
storage = DictStorage()

# Ajout des produits dans le stockage
storage.set_value(laptop.name, laptop.price)
storage.set_value(mouse.name, mouse.price)
storage.set_value(keyboard.name, keyboard.price)

# Affichage de tous les produits du stockage

for name, price in storage.all().items():
    print(f"name : {name}, price : {price}")

# Affichage du prix d'un produit spécifique
print(f" price : { storage.get_value('Laptop') } ")
# Affichage du total des prix 

total = 0
for v in storage.all().values(): total +=  v

print(f"Total prix : {total}")

# restore 
storage.restore("Mouse")
total = 0
for v in storage.all().values(): total +=  v
print(f"Total prix : {total}")

# reset
storage.reset()
total = 0
for v in storage.all().values(): total +=  v
print(f"Total prix : {total}")