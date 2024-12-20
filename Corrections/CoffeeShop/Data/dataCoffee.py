from Models.Product import Product

# Création des produits
coffee = Product(name="coffee", price=1.5)
tea = Product(name="tea", price=1.0)
milk = Product(name="milk", price=0.8)
cups = Product("cups", 0.1)
croissant = Product("croissants", 1.8)
napkins = Product("napkins", 0.02)
napkins2 = Product("napkins", 0.02) # hash identique à napkins donc napkins et napkins2 même clé

# Création du stock sous forme de dictionnaire chaque clé est unique voir la définition de l'objet Product
stock = {
    coffee: 50,
    tea: 30,
    milk: 20,
    cups: 90,
    croissant: 10,
    napkins: 100
}

# écrase la clé napkins car c'est pour Python le même hash d'objet
stock[napkins2] = 10
