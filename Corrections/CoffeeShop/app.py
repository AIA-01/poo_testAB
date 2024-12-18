from Models.Product import Product
from Data.dataCoffee import stock as data
from Infrastructures.Stock import Stock
from Services.CoffeeShop import CoffeeShop

# Test de CoffeeShop
stock = Stock(data)
coffee_shop = CoffeeShop(stock)

try:
    # Ajouter des produits au stock
    coffee = Product(name="Café Expresso", price=2.5)
    coffeeLatte = Product(name="Café latté", price=3.5)
    stock = coffee_shop.stock
    # on ajoute au stock les deux types de café avec leurs quantités respectives
    stock.add_product(coffee, 10)
    stock.add_product(coffeeLatte, 10)
    
    # Créer une commande et ajouter des produits
    order = coffee_shop.create_order()
    order.add_to_order(product=coffee, quantity=4)
    order.add_to_order(product=coffeeLatte, quantity=3)

    # Servir la commande
    print(coffee_shop.serve_order(order))  # Devrait afficher "Order served! Total: 20.5€"
    
except ValueError as e:  # Gestion de l'exception
    print(f"Erreur : {e}")