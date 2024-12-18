from Models.Product import Product

# Création des produits
coffee = Product(name="coffee", price=1.5)
tea = Product(name="tea", price=1.0)
milk = Product(name="milk", price=0.8)
cups = Product("cups", 0.1)
croissant = Product("croissants", 1.8)
napkins = Product("napkins", 0.02)

# Création du stock sous forme de dictionnaire chaque clé est unique voir la définition de l'objet Product
stock = {
    coffee: 50,
    tea: 30,
    milk: 20,
    cups: 90,
    croissant: 10,
    napkins: 100
}
