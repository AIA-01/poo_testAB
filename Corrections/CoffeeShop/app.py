
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
print( coffee_shop.serve_order(order) ) # Devrait afficher "Order served! Total: 7.5€"