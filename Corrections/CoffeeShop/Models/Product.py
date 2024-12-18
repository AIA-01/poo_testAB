from dataclasses import dataclass

@dataclass(eq=True, frozen=True)  # Ajoute immutabilité et support pour hashing
class Product:
    name: str
    price: float