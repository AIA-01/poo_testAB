### **Exercice 1 : Gestion d'un Rectangle**
**Objectif** : Apprenez à créer une classe simple avec des attributs et des méthodes.  
Créez une classe `Rectangle` qui permet de :  
1. Définir la largeur et la hauteur d’un rectangle.  
2. Calculer la surface du rectangle.  
3. Afficher les dimensions du rectangle.  

```python
PRECISION = 2
class Rectangle:

    # Constructeur avec paramètres obligatoires
    def __init__(self, width : float, lenght : float):
        self.width=width
        self.lenght=lenght
    
    def area(self) ->float:
        
        return  round( self.width * self.lenght, PRECISION )

    def __str__(self)->str:

        return f"Largeur : {self.width}, Hauteur : {self.lenght}"


p = Rectangle(2.98, 5.178)
print(p.area())
print(p)
```


**Instructions** :  
1. Créez une classe `Rectangle` avec deux attributs `largeur` et `hauteur`.  
2. Ajoutez une méthode `surface()` qui retourne la surface du rectangle.  
3. Ajoutez une méthode `afficher()` qui affiche les dimensions sous la forme : `Largeur : X, Hauteur : Y`.  

**Code attendu :**
```python
class Rectangle:
    pass
```

---

### **Exercice 2 : Gestion d'un Compte Bancaire**
**Objectif** : Créez une classe pour simuler un compte bancaire.  

**Instructions** :  
1. Créez une classe `CompteBancaire` avec un attribut `solde` initialisé à 0.  
2. Ajoutez une méthode `deposer(montant)` pour ajouter de l'argent au compte.  
3. Ajoutez une méthode `retirer(montant)` pour retirer de l'argent (si le solde est suffisant).  
4. Ajoutez une méthode `afficher_solde()` pour afficher le solde actuel.  

```python
class CompteBancaire:
    pass
```

---

### **Exercice 1 : Lancer un dé**
Simulez un lancer de dé à 6 faces. Faites une classe.

```python
import random as r 
```

1. Écrivez un programme qui simule le lancer d'un dé à 6 faces et affiche le résultat.

- **`r.randint(a, b)`** : génère un entier aléatoire entre `a` et `b`.