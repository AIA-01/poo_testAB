### **Pourquoi multiplie-t-on par 2 dans un test bilatéral ?**

Lorsqu'on effectue un **test bilatéral**, on cherche à savoir si une différence observée entre deux groupes est significative, **dans les deux directions possibles** : 

1. **Soit le groupe A est meilleur que le groupe B.**  
2. **Soit le groupe B est meilleur que le groupe A.**

C’est différent d’un **test unilatéral**, où l’on teste seulement une direction (par exemple, est-ce que A est meilleur que B, sans se préoccuper de B > A).

### **Rôle de la symétrie**
La plupart des tests statistiques reposent sur une courbe en forme de cloche (la **loi normale**), qui est **symétrique**. Cela signifie que :

- Les résultats extrêmes dans une direction (A > B) ont la même probabilité que les résultats extrêmes dans l'autre direction (B > A).

Dans un test bilatéral, pour être sûr de ne pas ignorer une différence dans une des deux directions, on doit **additionner les probabilités des deux extrêmes**. Comme elles sont symétriques, cela revient à **multiplier par 2** la probabilité calculée pour un côté.

---

### **Exemple simple avec des résultats**

#### **Scénario :**
Vous testez deux versions d'un site web :
- **Version A** : 200 visiteurs, 50 achats.
- **Version B** : 200 visiteurs, 60 achats.

Vous voulez savoir si la différence de taux de conversion (achats/visiteurs) est significative.

#### **Étapes :**

1. **Taux de conversion** :  
   - Version A : \( \frac{50}{200} = 0,25 \) (25 %).
   - Version B : \( \frac{60}{200} = 0,30 \) (30 %).  

   Différence de taux = \( 0,30 - 0,25 = 0,05 \) (5 points de pourcentage).

2. **Calcul de la p-value pour un test unilatéral** :  
   Supposons que vous obtenez une p-value de **0,03** pour la direction où B > A (Version B est meilleure).

3. **Test bilatéral :**  
   Puisque vous voulez vérifier **les deux directions** (B > A **ou** A > B), vous devez **multiplier par 2** :  
   \( \text{p-value bilatérale} = 0,03 \times 2 = 0,06 \).

4. **Conclusion :**  
   - Si votre seuil est de 5 % (\( \alpha = 0,05 \)), alors :  
     - Avec \( \text{p-value bilatérale} = 0,06 \), **la différence n'est pas significative**.  
   - Vous ne pouvez pas conclure que l’une des versions est meilleure.

---

### **Quand utiliser un test bilatéral ?**
Utilisez un **test bilatéral** quand **vous n’avez pas de préférence sur la direction de la différence**. Par exemple :
- Vous voulez savoir **si les conversions sont différentes**, sans supposer à l’avance quelle version est meilleure.
- Vous testez une hypothèse de manière exploratoire.
