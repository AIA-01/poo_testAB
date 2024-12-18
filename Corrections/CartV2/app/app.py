
# Importe la définition des classes ou fonction ou constante dans le script courant
from Models.Product import Product        
from Services.CartService import CartService

apple = Product(price = .5, name="Apple")
orange = Product(price = .7, name="Orange")

# Attention à penser à ajouter le storage
cart = CartService()

cart.buy(apple, 20)
cart.buy(apple, 20)
cart.buy(orange, 100)

# prix total 
print(cart.storage)
print(cart.total())

cart.restore(orange)
print(cart.total())

cart.reset()
print(cart.total())
