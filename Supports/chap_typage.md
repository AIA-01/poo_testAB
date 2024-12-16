### Introduction au module `typing` en Python

Le module `typing` permet d'ajouter des annotations de type dans le code Python, ce qui améliore la lisibilité, la compréhension et la maintenabilité du code. Bien que Python soit un langage dynamique, l'utilisation des annotations de type permet de rendre le code plus explicite, d'éviter certaines erreurs de type et d'améliorer l'intégration avec des outils comme les linters et les IDE.

Les annotations de type ne modifient pas le comportement du code, mais elles sont utiles pour la documentation, la vérification statique du type, et pour l'amélioration de l'autocomplétion dans les éditeurs de code.

### Types de base avec `typing`

1. **`int`, `float`, `str`, `bool`** : Ce sont des types de base que Python reconnaît déjà.
   ```python
   def add(a: int, b: int) -> int:
       return a + b
   ```

2. **`List`, `Dict`, `Tuple`, etc.** : Le module `typing` fournit des types génériques pour des collections comme les listes, dictionnaires, tuples, etc. Ces types permettent de préciser non seulement quel type de données la collection contiendra, mais aussi leur nombre ou leur structure.

### Exemples d'utilisation

#### 1. Liste d'entiers

```python
from typing import List

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

# Exemple d'appel
result = sum_list([1, 2, 3, 4])
print(result)  # Affiche 10
```

Dans cet exemple, nous spécifions que `numbers` est une liste d'entiers (`List[int]`), et que la fonction retourne un entier (`int`).

#### 2. Dictionnaire avec des types spécifiques

```python
from typing import Dict

def get_price(products: Dict[str, float]) -> float:
    total = sum(products.values())
    return total

# Exemple d'appel
product_prices = {"laptop": 1000.0, "mouse": 25.0}
total = get_price(product_prices)
print(total)  # Affiche 1025.0
```

Ici, le dictionnaire `products` a des clés de type `str` (nom du produit) et des valeurs de type `float` (prix du produit).

#### 3. Tuple

```python
from typing import Tuple

def get_coordinates() -> Tuple[float, float]:
    return (45.0, 7.0)

# Exemple d'appel
coords = get_coordinates()
print(coords)  # Affiche (45.0, 7.0)
```

Un `Tuple` est utilisé pour une collection ordonnée de types hétérogènes. Dans cet exemple, la fonction retourne un tuple contenant deux `float`.

#### 4. Union de types

```python
from typing import Union

def get_item(identifier: Union[int, str]) -> str:
    if isinstance(identifier, int):
        return f"Item ID: {identifier}"
    return f"Item Name: {identifier}"

# Exemple d'appel
print(get_item(10))  # Affiche "Item ID: 10"
print(get_item("apple"))  # Affiche "Item Name: apple"
```

L'`Union` permet de spécifier qu'un paramètre peut être de plusieurs types possibles. Ici, `identifier` peut être soit un `int`, soit une `str`.

#### 5. Optional (Type avec valeur `None`)

```python
from typing import Optional

def get_username(user_id: int) -> Optional[str]:
    # Supposons qu'on recherche l'utilisateur
    if user_id == 1:
        return "Alice"
    return None

# Exemple d'appel
username = get_username(1)
print(username)  # Affiche "Alice"

username = get_username(2)
print(username)  # Affiche "None"
```

`Optional[str]` est équivalent à `Union[str, None]`, indiquant que la fonction peut retourner soit un `str`, soit `None`.

### Pourquoi utiliser `typing` ?

- **Lisibilité** : Les annotations de type rendent le code plus facile à comprendre pour d'autres développeurs, car elles indiquent clairement quel type de données une fonction attend et retourne.
- **Vérification statique** : Des outils comme `mypy` permettent de vérifier les types avant l'exécution du programme, ce qui peut aider à détecter des erreurs de type.
- **Autocomplétion** : Les IDE peuvent utiliser les annotations de type pour proposer de meilleures suggestions lors de la saisie du code.
