from Infrastructures.Stock import Stock
from Services.Order import Order

class CoffeeShop:
    def __init__(self):
        self.stock = Stock()
        self.orders = []

    def create_order(self) -> Order:
        order = Order(self.stock)
        self.orders.append(order)
        return order

    def serve_order(self, order: Order) -> str:
        for product, quantity in order.items:
            self.stock.decrease_stock(product, quantity)
        return f"Order served! Total: {order.calculate_total()}€"
