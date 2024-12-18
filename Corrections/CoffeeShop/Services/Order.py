from Models.Product import Product
from typing import Dict
from Infrastructures.Stock import Stock
from Config.app import PRECISION


class Order:

    def __init__(self):
        self.storage: Dict[Product, float] = {}

    def add_to_order(self, product: Product, quantity: int) -> bool:
        if product in self.storage:
            self.storage[product] += quantity
        else:
            self.storage[product] = quantity

    def calculate_total(self) -> float:
        return sum(product.price * quantity for product, quantity in self.storage.items())

    def is_product_available(self, product: Product, quantity: int,  stock: Stock) -> bool:

        return stock.check_stock(product=product, quantity=quantity)
