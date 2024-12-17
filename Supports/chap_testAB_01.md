### **Introduction au Test A/B**

Le **test A/B** est une méthode utilisée pour **comparer deux versions d'une même situation** afin de déterminer laquelle est la plus performante. C'est très utilisé dans les domaines du marketing, des sites web ou des expériences scientifiques.

---

### **Exemple concret pour comprendre :**

Imaginons que vous avez un site web, et vous voulez savoir quelle version de votre page d'accueil attire **le plus de visiteurs**.  

- **Version A** : La page d'accueil actuelle (classique).  
- **Version B** : Une nouvelle page d'accueil (modifiée).  

Vous montrez **la version A** à un groupe de visiteurs et **la version B** à un autre groupe de visiteurs. Ensuite, vous mesurez combien de visiteurs cliquent sur un bouton pour acheter un produit.

---

### **Étapes d'un test A/B**

1. **Définir l'objectif** : Quel résultat veut-on comparer ? Par exemple, le nombre de clics, le nombre de ventes, etc.

2. **Créer deux versions** :  
   - **Version A** : la version actuelle (appelée **"contrôle"**).  
   - **Version B** : une version modifiée pour tester une amélioration.

3. **Séparer les participants** : Divisez les visiteurs en **deux groupes aléatoires** :  
   - Groupe 1 → voit **Version A**  
   - Groupe 2 → voit **Version B**

4. **Recueillir des données** : Comptez les résultats pour chaque groupe (nombre de clics, achats, etc.).

5. **Comparer les résultats** :  
   - Si la **Version B** obtient de meilleurs résultats que la **Version A**, alors la Version B est considérée comme plus efficace.  
   - Sinon, on garde la Version A.

---

### **Formule et résultats** (simplifié pour terminale)

On compare les **proportions** de réussite des deux groupes avec une analyse statistique.  
Les proportions peuvent être calculées par :  
$\text{Proportion} = \frac{\text{Nombre de succès}}{\text{Nombre total de participants}}$

**Exemple** :  
- **Version A** : 40 visiteurs sur 100 cliquent sur le bouton → proportion = $40 / 100 = 0,4$  
- **Version B** : 55 visiteurs sur 100 cliquent sur le bouton → proportion = $55 / 100 = 0,55$

**Conclusion** : La Version B a une meilleure proportion de succès (0,55 > 0,4), donc elle semble plus performante.

---

### **Exercice Python pour tester un A/B **

Voici un script pour simuler un test A/B avec deux groupes.

```python
import random

# Simuler un test A/B avec des succès aléatoires
def test_AB(taille_echantillon, taux_succes_A, taux_succes_B):
    groupe_A = [1 if random.random() < taux_succes_A else 0 for _ in range(taille_echantillon)]
    groupe_B = [1 if random.random() < taux_succes_B else 0 for _ in range(taille_echantillon)]

    # Calcul des proportions
    proportion_A = sum(groupe_A) / taille_echantillon
    proportion_B = sum(groupe_B) / taille_echantillon

    # Affichage des résultats
    print(f"Proportion de succès pour la Version A : {proportion_A:.2%}")
    print(f"Proportion de succès pour la Version B : {proportion_B:.2%}")

    # Conclusion
    if proportion_B > proportion_A:
        print("La Version B est plus performante.")
    elif proportion_B < proportion_A:
        print("La Version A est plus performante.")
    else:
        print("Les deux versions sont équivalentes.")

# Exemple avec 100 participants par groupe
test_AB(taille_echantillon=100, taux_succes_A=0.4, taux_succes_B=0.55)
```

---

### **Interprétation des résultats :**

Dans ce script :  
- La **Version A** a une probabilité de succès de 40 %.  
- La **Version B** a une probabilité de succès de 55 %.  

En exécutant le code plusieurs fois, on peut observer que la **Version B** est souvent plus performante, mais les résultats peuvent varier légèrement en raison du hasard.

---

### **Conclusion**

Le **test A/B** permet de comparer deux solutions (A et B) pour voir laquelle donne les meilleurs résultats.  
- Si une **différence significative** est observée, on choisit la version la plus efficace.  
- Le test repose sur des **proportions** et utilise parfois des outils statistiques plus avancés pour confirmer les résultats.  

C'est un outil simple mais puissant pour prendre des décisions basées sur des données réelles.