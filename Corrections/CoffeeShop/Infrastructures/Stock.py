from Models.Product import Product

class Stock:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if product.name in self.products:
            self.products[product.name] += quantity
        else:
            self.products[product.name] = quantity

    def check_stock(self, product: Product) -> int:
        return self.products.get(product.name, 0)

    def decrease_stock(self, product: Product, quantity: int) -> None:
        # error first
        if self.check_stock(product) < quantity:
            raise ValueError(f"Not enough stock for {product.name}")
        
        self.products[product.name] -= quantity
            