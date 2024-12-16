Voici un exemple d'A/B test **significatif** où la différence entre les groupes est suffisamment grande pour conclure que l'une des versions est meilleure que l'autre.

---

### **Situation**
- **Groupe A** : Une version de la page d'accueil affiche un bouton rouge.  
- **Groupe B** : Une autre version affiche un bouton vert.
- **Objectif (KPI)** : Mesurer le taux de clics sur le bouton (\% de visiteurs qui cliquent).

### **Données collectées**
- Groupe A (\( n_A = 500 \)) : \( \text{Taux de clics moyen} = 8\% \), \( \sigma_A = 2.5\%\).  
- Groupe B (\( n_B = 500 \)) : \( \text{Taux de clics moyen} = 10\% \), \( \sigma_B = 2.5\%\).

Nous voulons savoir si la différence de taux de clics (\( \Delta = 2\% \)) est significative ou simplement due au hasard.

---

### **Calculs**

#### 1. **Erreur standard combinée**
\[
SE = \sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}}
\]
\[
SE = \sqrt{\frac{(2.5)^2}{500} + \frac{(2.5)^2}{500}} = \sqrt{0.0125 + 0.0125} = \sqrt{0.025} = 0.158\%.
\]

#### 2. **Score \( Z \)**
\[
Z = \frac{\Delta}{SE} = \frac{10\% - 8\%}{0.158\%} = \frac{2\%}{0.158\%} \approx 12.66.
\]

#### 3. **Comparaison avec la valeur critique**
Pour un intervalle de confiance de 95 % (\( \alpha = 0.05 \)), le score critique \( Z_{\text{critique}} \) est 1.96.  
Ici, \( Z = 12.66 \) dépasse largement 1.96, ce qui signifie que la différence est très significative.

---

### **Interprétation**
La probabilité que cette différence soit due au hasard est quasi nulle (\( p \ll 0.05 \)). On peut conclure que la **version B** (bouton vert) a un taux de clics significativement meilleur que la version A (bouton rouge).

---

### **Visualisation**
Sur une courbe de loi normale centrée sur 0 (aucune différence), la différence observée (\( Z = 12.66 \)) est très loin à droite, en dehors de l'intervalle de confiance \([-1.96, +1.96]\). Cela illustre que la probabilité que cette différence soit due au hasard est extrêmement faible.

---

### **Conclusion**
- Vous pouvez implémenter la version B (bouton vert), car elle a prouvé être significativement meilleure.
- L'A/B test a permis d'optimiser le KPI (taux de clics) en choisissant la meilleure version.