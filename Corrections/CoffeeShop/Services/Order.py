from Models.Product import Product
from Infrastructures.Stock import Stock

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