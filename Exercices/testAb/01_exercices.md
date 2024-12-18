### **TP : Réaliser un A/B Testing et analyser les résultats**

### **Étapes du TP :**

#### **Étape 1 : Préparation des données**  

| Version | Nombre de visiteurs ($n$) | Achats ($c$) |
|---------|------------------------------|----------------|
| A       | 1000                        | 120            |
| B       | 1000                        | 140            |

Ces données montrent le nombre total de visiteurs et le nombre de conversions (achats) pour chaque version.

**Question 1 : Calculer les taux de conversion pour chaque version.**  
$Taux\ de\ conversion = \frac{Achats}{Nombre\ de\ visiteurs}$

#### **Étape 2 : Calcul des intervalles de confiance**  
À l’aide de la formule des intervalles de confiance pour une proportion :  
$IC = \hat{p} \pm Z \times \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$

**Question 2 : Calculer les intervalles de confiance à 95 % pour chaque version.**  
- Fournir les formules et expliquer comment les appliquer.  
- **Interprétation** : Vérifier si les intervalles se chevauchent.

---

#### **Étape 3 : Tester l’hypothèse (p-value)**  
Utiliser le **test Z** pour comparer les proportions.  
1. Calculer la proportion combinée 
   
$\hat{p}_{\text{pool}}$ :  
   
$\hat{p}_{\text{pool}} = \frac{n_A \times \hat{p}_A + n_B \times \hat{p}_B}{n_A + n_B}$

1. Calculer la statistique $Z$ :  
   
$Z = \frac{\hat{p}_A - \hat{p}_B}{\sqrt{\hat{p}_{\text{pool}} \times (1 - \hat{p}_{\text{pool}}) \times \left(\frac{1}{n_A} + \frac{1}{n_B}\right)}}$

2. Trouver la p-value associée au $Z$.  

**Question 3 : Quelle est la p-value, et comment l’interpréter ?**  
- Si $p < 0.05$, rejeter $H_0$.  
- Si $p \geq 0.05$, ne pas rejeter $H_0$.  

---

#### **Étape 4 : Conclusion**  
**Question 4 :**  
- Si les intervalles de confiance se chevauchent, pourquoi faut-il utiliser la p-value ?  
- Sur la base de la p-value, quelle version choisiriez-vous ?  
- Proposez des étapes futures : augmenter l’échantillon, tester d'autres hypothèses, etc.

---

### **Résultats attendus des étudiants**  
1. Calcul des taux de conversion et des intervalles de confiance.  
2. Décision basée sur la p-value (ou non) selon les résultats.  
3. Discussion sur les limites du test et les recommandations pour l’entreprise.

---

### **Bonus : Simuler les données avec Python**  
Les étudiants avancés peuvent coder une simulation pour générer des données et refaire les calculs. Exemple de script de départ :

```python
import numpy as np

# Simulation des données
np.random.seed(42)
visiteurs_A = 1000
visiteurs_B = 1000
achats_A = np.random.binomial(visiteurs_A, 0.12)
achats_B = np.random.binomial(visiteurs_B, 0.14)

print("Version A :", achats_A, "achats sur", visiteurs_A)
print("Version B :", achats_B, "achats sur", visiteurs_B)
```