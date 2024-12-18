from typing import Dict
from Models.Product import Product

class Stock:
    def __init__(self, storage: Dict[Product, float] = {}):
        self.storage: Dict[Product, float] = storage

    def add_product(self, product: Product, quantity: int):
        if product in self.storage:
            self.storage[product] += quantity
        else:
            self.storage[product] = quantity

    def check_stock(self, product : Product, quantity : int)->bool:
        return self.storage[product] >= quantity