### **Correction : Gestion d'un café - Système de commandes et de stock**

Voici la correction de l'exercice, structurée et progressive, avec toutes les classes implémentées et les tests associés.

---

### **1. Partie 1 : Créer la classe `Product`**

La classe `Product` représente un produit (une boisson dans le café). Chaque produit possède un nom et un prix.

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
```

**Explication :**
- Le constructeur initialise un produit avec un nom (`name`) et un prix (`price`).
- Cette classe est la base pour les autres classes et sera utilisée dans la gestion du stock et des commandes.

---

### **2. Partie 2 : Créer la classe `Stock`**

La classe `Stock` gère le stock des produits disponibles dans le café. Elle permet d'ajouter des produits et de vérifier la quantité disponible.

```python
class Stock:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if product.name in self.products:
            self.products[product.name] += quantity
        else:
            self.products[product.name] = quantity

    def check_stock(self, product: Product) -> int:
        return self.products.get(product.name, 0)

    def decrease_stock(self, product: Product, quantity: int) -> None:
        if self.check_stock(product) >= quantity:
            self.products[product.name] -= quantity
        else:
            raise ValueError(f"Not enough stock for {product.name}")
```

**Explication :**
- La méthode `add_product()` ajoute une quantité d'un produit dans le stock.
- La méthode `check_stock()` permet de vérifier la quantité d'un produit en stock.
- La méthode `decrease_stock()` diminue le stock d'un produit après qu'il ait été commandé.

**Test :**

```python
# Test du Stock
stock = Stock()
coffee = Product("Café Expresso", 2.5)
stock.add_product(coffee, 10)

print(stock.check_stock(coffee))  # Devrait afficher 10
```

---

### **3. Partie 3 : Créer la classe `Order`**

La classe `Order` représente une commande. Elle permet d'ajouter des produits à la commande, de calculer le total et de vérifier si les produits sont en stock.

```python
class Order:
    def __init__(self, stock: Stock):
        self.items = []
        self.stock = stock

    def add_to_order(self, product: Product, quantity: int) -> None:
        if self.stock.check_stock(product) >= quantity:
            self.items.append((product, quantity))
        else:
            raise ValueError(f"Not enough stock for {product.name}")

    def calculate_total(self) -> float:
        return sum(product.price * quantity for product, quantity in self.items)

    def is_product_available(self, product: Product, quantity: int) -> bool:
        return self.stock.check_stock(product) >= quantity
```

**Explication :**
- La méthode `add_to_order()` ajoute un produit à la commande si la quantité est disponible en stock.
- La méthode `calculate_total()` calcule le total de la commande en multipliant le prix de chaque produit par la quantité commandée.
- La méthode `is_product_available()` vérifie si un produit est disponible en quantité suffisante.

**Test :**

```python
# Test de Order
order = Order(stock)
order.add_to_order(coffee, 2)

print(order.calculate_total())  # Devrait afficher 5.0
```

---

### **4. Partie 4 : Créer la classe `CoffeeShop`**

La classe `CoffeeShop` est la classe principale qui gère le processus de commande et de stock dans le café. Elle crée des commandes, sert des produits, et met à jour le stock.

```python
class CoffeeShop:
    def __init__(self):
        self.stock = Stock()
        self.orders = []

    def create_order(self) -> Order:
        order = Order(self.stock)
        self.orders.append(order)
        return order

    def serve_order(self, order: Order) -> None:
        for product, quantity in order.items:
            self.stock.decrease_stock(product, quantity)
        print(f"Order served! Total: {order.calculate_total()}€")
```

**Explication :**
- La méthode `create_order()` crée une nouvelle commande et l'ajoute à la liste des commandes.
- La méthode `serve_order()` sert une commande, met à jour le stock et affiche le total de la commande.

**Test :**

```python
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
coffee_shop.serve_order(order)  # Devrait afficher "Order served! Total: 7.5€"
```

---
