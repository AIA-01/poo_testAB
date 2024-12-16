from Models.Product import Product

class CartService:
    
    def __init__(self):
        self.storage = {}

    def buy(self, product : Product, quantity : int ):
        
        if product.name in self.storage:
            self.storage[product.name] += quantity * product.price 
        else:
             self.storage[product.name] = quantity * product.price 
             
    def total(self):
        total = 0
        
        for name, price in self.storage.items():
            total += price 
        
        return total 
    
    def reset(self) -> None:
        self.storage.clear()
        
    def restore(self, product: Product):
        if product.name in self.storage:
            del self.storage[product.name] 