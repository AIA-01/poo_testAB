### Exercices Python : Boucles, Fonctions, Classes et Compréhensions de listes

#### **Exercice 1 : Afficher les nombres pairs**
Ecrivez un programme qui affiche tous les nombres pairs entre 1 et 20 inclus.

**Correction :**
```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

#### **Exercice 2 : Somme des éléments d'une liste**
Créez une fonction qui prend une liste de nombres en paramètre et retourne la somme des éléments.

**Correction :**
```python
def somme_liste(liste):
    return sum(liste)

print(somme_liste([1, 2, 3, 4, 5]))  # 15
```

#### **Exercice 3 : Factorielle avec une boucle**
Écrivez une fonction qui calcule la factorielle d'un nombre donné.

**Correction :**
```python
def factorielle(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorielle(5))  # 120
```

#### **Exercice 4 : Compter les voyelles**
Écrivez une fonction qui compte le nombre de voyelles dans une chaîne de caractères.

**Correction :**
```python
def compter_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    return sum(1 for char in chaine if char in voyelles)

print(compter_voyelles("Bonjour"))  # 3
```

#### **Exercice 5 : Classe Rectangle**
Créez une classe `Rectangle` avec des attributs longueur et largeur, et une méthode pour calculer l'aire.

**Correction :**
```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        return self.longueur * self.largeur

rect = Rectangle(5, 3)
print(rect.calculer_aire())  # 15
```

#### **Exercice 6 : Inverser une chaîne**
Écrivez une fonction qui inverse une chaîne de caractères donnée.

**Correction :**
```python
def inverser_chaine(chaine):
    return chaine[::-1]

print(inverser_chaine("Python"))  # nohtyP
```

#### **Exercice 7 : Trouver le maximum dans une liste**
Écrivez une fonction qui trouve le plus grand élément dans une liste.

**Correction :**
```python
def trouver_max(liste):
    return max(liste)

print(trouver_max([3, 5, 2, 9, 1]))  # 9
```

#### **Exercice 8 : Carrés des nombres avec une compréhension de liste**
Créez une liste contenant les carrés des nombres de 1 à 10 inclus en utilisant une compréhension de liste.

**Correction :**
```python
carres = [i**2 for i in range(1, 11)]
print(carres)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

#### **Exercice 9 : Liste des nombres impairs**
Générez une liste contenant tous les nombres impairs entre 1 et 20 inclus en utilisant une compréhension de liste.

**Correction :**
```python
impairs = [i for i in range(1, 21) if i % 2 != 0]
print(impairs)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

#### **Exercice 10 : Classe Cercle avec périmètre et aire**
Créez une classe `Cercle` avec un attribut rayon, une méthode pour calculer le périmètre et une autre pour l'aire.

**Correction :**
```python
import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

cercle = Cercle(5)
print(cercle.perimetre())  # 31.41592653589793
print(cercle.aire())  # 78.53981633974483
```

Voici des exercices plus avancés, incluant des structures de données et l'utilisation de NumPy :

### **Exercice 11 : Tri des valeurs uniques d'une liste**
Écrivez une fonction qui prend une liste, extrait ses valeurs uniques, et les trie par ordre croissant.

**Correction :**
```python
def trier_uniques(liste):
    return sorted(set(liste))

print(trier_uniques([4, 2, 6, 2, 7, 6, 1]))  # [1, 2, 4, 6, 7]
```

---

### **Exercice 12 : Histogramme des fréquences**
Écrivez une fonction qui prend une liste et retourne un dictionnaire représentant les fréquences de chaque élément.

**Correction :**
```python
from collections import Counter

def histogramme(liste):
    return dict(Counter(liste))

print(histogramme([1, 2, 2, 3, 3, 3, 4]))  # {1: 1, 2: 2, 3: 3, 4: 1}
```

---

### **Exercice 13 : Matrice identité (NumPy)**
Utilisez NumPy pour créer une matrice identité de taille donnée.

**Correction :**
```python
import numpy as np

def matrice_identite(n):
    return np.eye(n)

print(matrice_identite(4))
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
```

---

### **Exercice 14 : Produit matriciel (NumPy)**
Créez deux matrices aléatoires avec NumPy et calculez leur produit matriciel.

**Correction :**
```python
import numpy as np

def produit_matriciel():
    A = np.random.randint(1, 10, (3, 3))
    B = np.random.randint(1, 10, (3, 3))
    produit = np.dot(A, B)
    return A, B, produit

A, B, produit = produit_matriciel()
print("Matrice A:\n", A)
print("Matrice B:\n", B)
print("Produit matriciel:\n", produit)
```

---

### **Exercice 15 : Trouver les valeurs manquantes**
Écrivez une fonction qui identifie les indices des valeurs manquantes (NaN) dans un tableau NumPy.

**Correction :**
```python
import numpy as np

def valeurs_manquantes(array):
    return np.where(np.isnan(array))

array = np.array([1, 2, np.nan, 4, np.nan])
print(valeurs_manquantes(array))  # (array([2, 4]),)
```

---

### **Exercice 16 : Inversion d’un dictionnaire**
Écrivez une fonction qui inverse un dictionnaire (les clés deviennent des valeurs et vice versa).

**Correction :**
```python
def inverser_dictionnaire(dico):
    return {val: key for key, val in dico.items()}

print(inverser_dictionnaire({"a": 1, "b": 2, "c": 3}))  # {1: 'a', 2: 'b', 3: 'c'}
```

---

### **Exercice 17 : Matrice de distances (NumPy)**
Générez une matrice représentant les distances euclidiennes entre des points dans un espace 2D.

**Correction :**
```python
import numpy as np

def matrice_distances(points):
    n = len(points)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distances[i, j] = np.linalg.norm(points[i] - points[j])
    return distances

points = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
print(matrice_distances(points))
```

---

### **Exercice 18 : Implémenter une pile (Stack)**
Créez une classe `Pile` qui simule une pile (LIFO : Last In, First Out).

**Correction :**
```python
class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, valeur):
        self.elements.append(valeur)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        raise IndexError("La pile est vide")

    def est_vide(self):
        return len(self.elements) == 0

pile = Pile()
pile.empiler(5)
pile.empiler(10)
print(pile.depiler())  # 10
print(pile.est_vide())  # False
```

---

### **Exercice 19 : Statistiques sur un tableau NumPy**
Écrivez une fonction qui retourne la moyenne, la médiane, et l'écart-type d'un tableau NumPy.

**Correction :**
```python
import numpy as np

def statistiques_tableau(array):
    return {
        "moyenne": np.mean(array),
        "médiane": np.median(array),
        "écart-type": np.std(array)
    }

array = np.array([1, 2, 3, 4, 5])
print(statistiques_tableau(array))
```

---

### **Exercice 20 : Recherche dans un graphe (DFS)**
Implémentez l'algorithme de recherche en profondeur (DFS) pour parcourir un graphe représenté par un dictionnaire.

**Correction :**
```python
def dfs(graphe, noeud, visites=None):
    if visites is None:
        visites = set()
    visites.add(noeud)
    print(noeud, end=" ")
    for voisin in graphe[noeud]:
        if voisin not in visites:
            dfs(graphe, voisin, visites)

graphe = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}
dfs(graphe, "A")  # A B D E C F
```