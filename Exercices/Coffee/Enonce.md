### **Exercice : Gestion d'un café - Système de commandes et de stock**

Organisez le code en structurant le projet.

Pour tester votre code, consultez le fichier `app.py`.

---

### **1. Partie 1 : Créer la classe `Product`**

**Objectif :** Créer une classe `Product` qui représente une boisson dans le café, avec un nom et un prix.

**Étapes :**
- Créez une classe `Product` avec un constructeur qui prend un nom (`name`) et un prix (`price`) comme arguments.
- Implémentez des méthodes pour accéder à ces propriétés.

**Conseil :**
- Utilisez un format de prix en **float** pour les boissons.

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
```

---

### **2. Partie 2 : Créer la classe `Stock`**

**Objectif :** Créer un système de gestion de stock qui permet d'ajouter des produits et de vérifier les quantités disponibles.

**Étapes :**
- Créez une classe `Stock` qui contient un dictionnaire pour stocker les produits et leurs quantités.
- Ajoutez une méthode `add_product()` pour ajouter des produits au stock.
- Ajoutez une méthode `check_stock()` qui permet de vérifier si un produit est disponible en quantité suffisante.

```python
class Stock:
    pass
```

---

### **3. Partie 3 : Créer la classe `Order`**

**Objectif :** Créer une classe `Order` qui représente une commande dans le café. Elle permettra d'ajouter des produits à la commande, de calculer le total et de vérifier si les produits sont en stock.

**Étapes :**
- Créez une classe `Order` qui contient une liste des produits commandés.
- Ajoutez une méthode `add_to_order()` pour ajouter un produit à la commande.
- Ajoutez une méthode `calculate_total()` pour calculer le total de la commande en fonction des produits ajoutés.
- Ajoutez une méthode `is_product_available()` pour vérifier si un produit est disponible en stock avant de l’ajouter à la commande.

```python
class Order:
    pass
```

---

### **4. Partie 4 : Créer la classe `CoffeeShop`**

**Objectif :** Créer la classe principale `CoffeeShop`, qui permettra de gérer l'ensemble du processus, de l'ajout de stock à la prise de commande.

**Étapes :**
- Créez une classe `CoffeeShop` qui contient une instance de `Stock` et une instance de `Order`.
- Implémentez une méthode `create_order()` pour créer une nouvelle commande.
- Implémentez une méthode `serve_order()` pour servir la commande et la retirer du stock.

```python
class CoffeeShop:
    pass
```

---

### **5. Fichier `app.py`**

```python
from Services.CoffeeShop import CoffeeShop
from Models.Product import Product

# Test de CoffeeShop
coffee_shop = CoffeeShop()

# Ajouter des produits au stock
coffee = Product("Café Expresso", 2.5)
stock = coffee_shop.stock
stock.add_product(coffee, 10)

# Créer une commande et ajouter des produits
order = coffee_shop.create_order()
order.add_to_order(coffee, 3)

# Servir la commande
print(coffee_shop.serve_order(order))  # Devrait afficher "Order served! Total: 7.5€"
```

---

### Changements effectués :
1. Correction des fautes grammaticales et typographiques.
2. Ajout de quelques clarifications pour une meilleure lisibilité.
3. Suppression des phrases ambiguës ou incomplètes pour plus de cohérence.
