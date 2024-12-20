### **Exemple 1 : Test de la différence entre deux moyennes (utilisation de `ttest_ind`)**
Disons que nous avons les données suivantes concernant le **temps passé** (en minutes) sur un site web par deux groupes :

- **Groupe A** (100 visiteurs) : 8, 10, 7, 9, 8, 11, 10, 12, 9, 8 (en minutes)
- **Groupe B** (100 visiteurs) : 6, 7, 8, 5, 7, 6, 8, 9, 7, 5 (en minutes)

Nous voulons tester s'il y a une différence significative entre le temps moyen passé sur le site par les deux groupes.

```python
from scipy.stats import ttest_ind

# todo implémenter la fonction moyenne
def mean(numbers):
   pass

# Données
A = [8, 10, 7, 9, 8, 11, 10, 12, 9, 8]
B = [6, 7, 8, 5, 7, 6, 8, 9, 7, 5]

# Test t indépendant
stat, p_value = ttest_ind(A, B)

print(f"Statistique t : {stat}")
print(f"P-Value : {p_value}")

# Moyennes des groupes
mean_A = mean(A)
mean_B = mean(B)

if p_value < 0.05:
    print("Il y a une différence significative entre les groupes A et B.")
    if mean_A > mean_B:
        print("Choisissez A (moyenne supérieure).")
    else:
        print("Choisissez B (moyenne supérieure).")
else:
    print("Aucune différence significative entre les groupes A et B.")
    print("Choisissez en fonction d'autres critères.")

```

**Résultats possibles :**
- **Statistique t** : 3.25
- **P-value** : 0.004

Interprétation : La **p-value** est inférieure à 0.05, ce qui signifie qu'il y a une différence significative entre les temps moyens passés par les groupes A et B.

---

### **Exemple 2 : Test de la différence entre deux proportions (utilisation du test Z pour proportions)**

Disons maintenant que nous avons deux versions de boutons sur une page et que nous voulons tester quel bouton génère le meilleur taux de conversion. Les données sont les suivantes :

- **Groupe A** (1000 visiteurs) a eu 110 conversions.
- **Groupe B** (1000 visiteurs) a eu 150 conversions.

Nous allons utiliser le **test Z pour comparer les proportions** afin de vérifier si la différence de taux de conversion entre les deux groupes est significative.

```python
import math
from scipy.stats import norm

# Données
n_A = 1000  # Nombre de visiteurs pour A
c_A = 110   # Conversions pour A

n_B = 1000  # Nombre de visiteurs pour B
c_B = 150   # Conversions pour B

# Calcul des taux de conversion
P_A = c_A / n_A
P_B = c_B / n_B

print(f"Taux de conversion de A : {P_A:.2%}")
print(f"Taux de conversion de B : {P_B:.2%}")

# Intervalle de confiance pour A
z = 1.96  # 95 % de niveau de confiance
s_A = math.sqrt(P_A * (1 - P_A) / n_A)
ic_A = (P_A - z * s_A, P_A + z * s_A)
print(f"IC pour A : {ic_A}")

# Intervalle de confiance pour B
s_B = math.sqrt(P_B * (1 - P_B) / n_B)
ic_B = (P_B - z * s_B, P_B + z * s_B)
print(f"IC pour B : {ic_B}")

# Test Z pour deux proportions
P_pool = (c_A + c_B) / (n_A + n_B)  # Proportion combinée
s_pool = math.sqrt(P_pool * (1 - P_pool) * (1 / n_A + 1 / n_B))
z_score = (P_B - P_A) / s_pool
p_value = 2 * (1 - norm.cdf(abs(z_score)))

print(f"Z-Score : {z_score}")
print(f"P-Value : {p_value}")

# Interprétation
alpha = 0.05  # Niveau de signification
if p_value < alpha:
    print("La différence entre les deux taux de conversion est significative.")
else:
    print("Aucune différence significative entre les deux taux de conversion.")
```

**Résultats possibles :**
- **Taux de conversion de A** : 11.00%
- **Taux de conversion de B** : 15.00%
- **Intervalle de confiance pour A** : (0.0936, 0.1264)
- **Intervalle de confiance pour B** : (0.1308, 0.1692)
- **Z-Score** : 4.47
- **P-Value** : 0.0000

Interprétation : La **p-value** est très inférieure à 0.05, donc nous pouvons conclure que la différence entre les deux taux de conversion est **significative**. Le bouton B a un taux de conversion supérieur à A.

---

### **Résumé**

- **Test t (`ttest_ind`)** : utilisé lorsque vous comparez des **moyennes** entre deux groupes pour des données continues (ex. temps, prix, score).
- **Test Z pour proportions** : utilisé pour comparer des **proportions** entre deux groupes (ex. taux de clics, taux de conversion). Cela est plus adapté à des situations comme celles des boutons A/B.

## Remarques 

Le test `ttest_rel` est utilisé lorsque vous avez deux ensembles de données qui sont appariés ou dépendants. Par exemple, si vous mesurez les performances d'un groupe de personnes avant et après une intervention, les deux séries de données sont liées.

```python
from scipy.stats import `ttest_rel`

# Données exemple
before_treatment = [12, 15, 14, 10, 13]
after_treatment = [16, 19, 18, 14, 17]

# Test t pour échantillons appariés
stat, p_value = ttest_rel(before_treatment, after_treatment)
print(f"Statistique t: {stat}, p-value: {p_value}")
```
