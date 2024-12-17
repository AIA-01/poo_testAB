from Models.Product import Product
from Infrastructures.DictStorage import DictStorage
from Services.CartService import CartService

apple =  Product(name="Apple", price=.7)
orange = Product(name="Orange", price=.9)

cart = CartService(DictStorage())

cart.buy(apple, 10)
cart.buy(orange, 20)

print(cart.total())