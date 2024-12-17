# Classe principale du service panier
class CartService:
    def __init__(self, storage):
        self.storage = storage

    def buy(self, product, quantity: int) -> None:
        """
        Permet d'acheter un produit en spécifiant une quantité.
        Si la quantité est inférieure ou égale à 0, une erreur est levée.
        Enregistre la valeur totale du produit dans le stockage.
        :param product: Le produit à acheter.
        :param quantity: La quantité à acheter.
        :raises ValueError: Si la quantité est invalide (inférieure ou égale à zéro).
        """
        # Vérification de la quantité
        q = abs(int(quantity))
        if q <= 0:
            raise ValueError("bad quantity command")

        # Enregistrement de la valeur totale dans le stockage
        

    def total(self) -> float:
        """
        Calcule le prix total TTC de tous les produits dans le panier.
        :return: Le prix total TTC.
        """
        total = 0

        # Récupération des produits commandés dans le stockage

        return total

    def reset(self) -> None:
        """
        Réinitialise la commande en supprimant tous les produits du panier.
        """

    def restore(self, name: str) -> None:
        """
        Supprime un produit du panier en fonction de son nom.
        :param name: Le nom du produit à supprimer.
        """