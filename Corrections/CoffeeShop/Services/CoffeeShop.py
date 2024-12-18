from Infrastructures.Stock import Stock
from Services.Order import Order

class CoffeeShop:

    def __init__(self, stock : Stock):
        self.stock = stock

    def create_order(self):
        return Order()
    
    def serve_order(self, order : Order)->str:
        for product, quantity in order.storage.items():
            if not order.is_product_available(product, quantity, self.stock):
                raise ValueError(f"Une quantité commandée dépasse le stock {product.name}")
            
            # mise à jour du stock
            self.stock.storage[product] = self.stock.storage[product] - quantity 
            
        total=order.calculate_total()
        
        return f"Order served! Total: {total}€" 