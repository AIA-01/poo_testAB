from dataclasses import dataclass

@dataclass(eq=True, frozen=True)  # Ajoute immutabilité et support pour hashing permet de définir des clés dans les dictionnaires , un objet unique une clé unique
class Product:
    name: str
    price: float
