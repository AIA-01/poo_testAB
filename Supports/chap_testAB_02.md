### **Introduction au Test A/B avec la notion d'intervalle de confiance** (niveau terminale)

Le **test A/B** est une méthode utilisée pour comparer deux versions d'une situation (par exemple, une page web, une publicité, ou un produit) afin de déterminer laquelle fonctionne le mieux. **L'intervalle de confiance** permet ici de s'assurer que la différence observée entre les deux versions est **statistiquement significative** et non due au hasard.

---

### **Contexte avec un exemple :**

**Situation** :  
Un site web veut tester deux versions d’une page d’accueil :  
- **Version A** : la page actuelle.  
- **Version B** : une nouvelle version améliorée.  

Objectif : Mesurer le pourcentage de visiteurs qui cliquent sur un bouton d'achat.  
- **Groupe 1** voit la **Version A** (100 visiteurs).  
- **Groupe 2** voit la **Version B** (100 visiteurs).  

Les résultats sont les suivants :  
- 40 visiteurs sur 100 cliquent sur la version A → proportion $p_A = 40\% = 0,4$.  
- 55 visiteurs sur 100 cliquent sur la version B → proportion $p_B = 55\% = 0,55$.

---

### **Intervalle de confiance pour les proportions**

Pour déterminer si la différence entre les deux versions est significative, on utilise un **intervalle de confiance** pour chacune des proportions $p_A$ et $p_B$.

#### **Formule de l'intervalle de confiance pour une proportion :**  
$IC = p \pm z \times \sqrt{\frac{p(1-p)}{n}}$
Où :  
- $p$ = proportion observée (succès/nombre total).  
- $n$ = taille de l’échantillon.  
- $z$ = valeur liée au niveau de confiance (exemple : 1,96 pour un niveau de confiance à 95 %).

---

### **Étape par étape :**

1. **Calcul de l'intervalle de confiance pour la Version A :**  
   - $p_A = 0,4$, $n_A = 100$, $z = 1,96$ pour un niveau de confiance de 95 %.  
   - L’erreur standard est :  
     $SE_A = \sqrt{\frac{p_A (1 - p_A)}{n_A}} = \sqrt{\frac{0,4 \times (1 - 0,4)}{100}} = 0,049$
   - L'intervalle de confiance est :  
     $IC_A = 0,4 \pm 1,96 \times 0,049 = [0,303; 0,497]$

1. **Calcul de l'intervalle de confiance pour la Version B :**  
   - $p_B = 0,55$, $n_B = 100$, $z = 1,96$.  
   - L’erreur standard est :  
     $SE_B = \sqrt{\frac{p_B (1 - p_B)}{n_B}} = \sqrt{\frac{0,55 \times (1 - 0,55)}{100}} = 0,0497$
   - L'intervalle de confiance est :  
     $IC_B = 0,55 \pm 1,96 \times 0,0497 = [0,453; 0,647]$

---

### **Interprétation des résultats**

- L'intervalle de confiance pour **Version A** est **[30,3 % ; 49,7 %]**.  
- L'intervalle de confiance pour **Version B** est **[45,3 % ; 64,7 %]**.

**Que remarque-t-on ?**  
Les intervalles de confiance ne se chevauchent **pas**. Cela signifie que la différence entre les deux proportions (40 % pour A et 55 % pour B) est **statistiquement significative** au niveau de confiance de 95 %.  
On peut donc conclure que la **Version B est plus performante** que la Version A.

---

### **Exercice Python pour tester ces intervalles**

Faites un programme Python pour **calculer les intervalles de confiance** et les comparer.

```python
import math

class TestAB:
  pass
```

---

### **Conclusion simplifiée pour les élèves**

1. Le **test A/B** permet de comparer deux proportions pour voir laquelle est meilleure.  
2. L'**intervalle de confiance** permet de mesurer la fiabilité de ces proportions.  
3. Si les intervalles de confiance **ne se chevauchent pas**, alors la différence est **significative**.  

Ainsi, grâce à l'intervalle de confiance, on peut conclure avec rigueur que la **Version B est plus efficace que la Version A**.