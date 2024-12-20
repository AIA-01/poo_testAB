### **Exercice 1 : Calcul des intervalles de confiance pour des moyennes**
Vous réalisez un test A/B pour comparer le taux de conversion de deux versions d'une page web. Les données suivantes sont collectées :  
- Version A : $n_A = 1000$, $\bar{x}_A = 0.05$, $\sigma_A = 0.01$  
- Version B : $n_B = 1200$, $\bar{x}_B = 0.055$, $\sigma_B = 0.012$  

**Objectifs :**
1. Calculez les intervalles de confiance à 95 % pour les deux versions.
2. Déterminez s’il y a un chevauchement des intervalles de confiance.
3. Affichez si la différence est statistiquement significative ou non en vous basant sur ce chevauchement.

*Indice : Utilisez la formule de l'intervalle de confiance pour une moyenne :*  
$IC = \bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}}$  
*Avec $z \approx 1.96$ pour un intervalle à 95 %.*

---

### **Exercice 2 : Test de différence avec p-value**
Vous réalisez un test A/B pour évaluer le temps moyen passé sur deux versions d'une application mobile. Les données suivantes sont observées :  
- Version A : $n_A = 50$, $\bar{x}_A = 120$, $\sigma_A = 15$  
- Version B : $n_B = 55$, $\bar{x}_B = 125$, $\sigma_B = 10$  

**Objectifs :**
1. Formulez les hypothèses $H_0$ et $H_1$ pour ce test.
2. Calculez la statistique de test (test t).
3. Calculez la p-value et déterminez si vous rejetez $H_0$ à un seuil de 5 %.

*Indice : Utilisez la formule pour la statistique de test t dans le cas de deux échantillons indépendants :*  
$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}}}$  
*Pour la p-value, utilisez une fonction comme `scipy.stats.t.sf`.*

---

### **Exercice 3 : Identification de chevauchements dans plusieurs tests A/B**
Vous avez réalisé trois tests A/B pour comparer la performance de différentes versions d’une interface utilisateur. Les intervalles de confiance à 95 % pour chaque test sont donnés :  
- Test 1 : Version A [0.3, 0.5] et Version B [0.45, 0.6]  
- Test 2 : Version A [0.1, 0.2] et Version B [0.25, 0.35]  
- Test 3 : Version A [0.4, 0.55] et Version B [0.5, 0.65]  

**Objectifs :**
1. Écrivez une fonction Python qui détermine si deux intervalles se chevauchent.  
2. Utilisez cette fonction pour analyser chacun des trois tests.  
3. Pour chaque test, affichez un message indiquant si les intervalles se chevauchent ou non, et donc si les performances des versions peuvent être considérées comme statistiquement différentes.

*Indice : Deux intervalles $[a, b]$ et $[c, d]$ se chevauchent si*  
$\max(a, c) \leq \min(b, d)$

---

### Exercice 4 : Diviser l'audience en deux groupes (Groupe A et Groupe B)**

L'objectif ici est de simuler l'attribution aléatoire des utilisateurs à deux groupes, A et B. Vous utiliserez une fonction Python pour distribuer aléatoirement les utilisateurs.

**Instructions** :
1. Créez une fonction `assign_group(user_id)` qui attribue chaque utilisateur à un groupe A ou B de manière aléatoire.
2. Générez une liste d'utilisateurs (par exemple, 10 utilisateurs).
3. Utilisez un dictionnaire pour associer chaque utilisateur à son groupe.

```python
import random

```

---

#### Suivre les performances des deux versions**

Simulez ou utilisez des données réelles pour suivre les performances des groupes A et B. Par exemple, le nombre de clics sur un bouton par jour.

**Instructions** :
1. Créez un dictionnaire `results` avec les performances de chaque groupe sur plusieurs jours (par exemple, le nombre de clics).
2. Calculez la moyenne des performances pour chaque groupe (A et B).

```python
# Simuler les résultats des deux groupes (clics par jour)
results = {'A': [10, 15, 20], 'B': [12, 18, 25]}  # Exemple de données

```

---

#### Analyser les résultats statistiquement

L’objectif ici est d’utiliser un test statistique pour savoir si les différences observées entre les groupes sont significatives.

**Instructions** :
1. Utilisez le **test t de Student** pour comparer les performances des groupes A et B.
2. Interprétez le p-value pour savoir si les résultats sont statistiquement significatifs.

```python
from scipy.stats import ttest_ind

```

---

#### Visualiser les résultats**

Une bonne visualisation des résultats permet de mieux comprendre les performances des deux groupes sur le temps.

**Instructions** :
1. Utilisez `matplotlib` pour tracer les performances de chaque groupe au cours des jours.
2. Comparez les deux courbes pour voir si la version B surperforme la version A.

```python
```

---

#### Automatiser et itérer**

L’objectif ici est d’automatiser le processus de test A/B pour des itérations futures.

**Instructions** :
1. Créez une fonction `run_ab_test(group_a, group_b)` qui exécute le test t de Student et renvoie la statistique et la p-value.
2. Testez cette fonction avec plusieurs groupes de données.

```python
```

---