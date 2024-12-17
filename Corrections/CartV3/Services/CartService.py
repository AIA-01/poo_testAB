from Models.Product import Product

# Classe principale du service panier
class CartService:
    
    def __init__(self, storage):
        self.storage = storage

    def buy(self, product : Product , quantity: int) -> None:
        # Vérification de la quantité
        q = abs(int(quantity))
        if q <= 0:
            raise ValueError("bad quantity command")

        # Enregistrement de la valeur totale dans le stockage
        total = round(product.price * q, 2)
        
        self.storage.set_value(product.name, total)

    def total(self) -> float:
        return self.storage.total()

    def reset(self) -> None:
        self.storage.reset()

    def restore(self, product : Product) -> None:
        self.storage.restore(product.name)