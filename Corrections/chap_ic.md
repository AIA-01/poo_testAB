### Exercice : Introduction à l'intervalle de confiance

**Contexte**  
Un sondage est réalisé auprès de 50 élèves pour estimer leur temps moyen de révision (en heures) avant un examen. Les résultats montrent une moyenne de **3,5 heures** avec un écart-type de **0,8 heure**.

---

#### Questions

1. Calculez un **intervalle de confiance à 95 %** pour le temps moyen de révision des élèves de la population entière.  
2. Que signifie cet intervalle dans le contexte de l'étude ?

---

#### Formule à utiliser

L'intervalle de confiance pour la moyenne est donné par :  
$IC = \bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}}$
où :  
- $\bar{x}$ : moyenne de l'échantillon  
- $\sigma$ : écart-type de l'échantillon  
- $n$ : taille de l'échantillon  
- $z$ : valeur associée au niveau de confiance (95 % → $z = 1,96$)  

---

### Étape guidée pour Terminale  

#### Étape 1 : Rassemblez les données
- Moyenne ($\bar{x}$) = 3,5 heures  
- Écart-type ($\sigma$) = 0,8 heure  
- Taille de l'échantillon ($n$) = 50  
- Niveau de confiance = 95 % ($z = 1,96$)  

#### Étape 2 : Appliquez la formule
- Calcul de l'erreur type :  
$\text{Erreur type} = \frac{\sigma}{\sqrt{n}}$  
- Calcul de l'intervalle :  
  $IC = \bar{x} \pm z \cdot \text{Erreur type}$  

---

### Correction sous forme de code Python simple

Voici une version Python simplifiée pour résoudre cet exercice, compréhensible au niveau terminale.

```python
import math

# Données
moyenne = 3.5  # Moyenne de l'échantillon
ecart_type = 0.8  # Écart-type de l'échantillon
taille_echantillon = 50  # Taille de l'échantillon
z = 1.96  # Valeur critique pour 95 % de confiance

# Calcul de l'erreur type
erreur_type = ecart_type / math.sqrt(taille_echantillon)

# Calcul des bornes de l'intervalle de confiance
borne_inferieure = moyenne - z * erreur_type
borne_superieure = moyenne + z * erreur_type

# Résultat
print(f"Intervalle de confiance à 95 % : [{borne_inferieure:.2f}, {borne_superieure:.2f}] heures")
```

---

### Résultats attendus
Pour cet exemple :  
- **Erreur type** :  
$\frac{0,8}{\sqrt{50}} \approx 0,113$
- **Intervalle de confiance** :  
$IC = 3,5 \pm 1,96 \cdot 0,113 \approx [3,28, 3,72]$

---

### Interprétation

Avec un niveau de confiance de 95 %, on peut affirmer que le **temps moyen de révision de tous les élèves** de la population se situe probablement entre **3,28 heures et 3,72 heures**. Cela signifie que si on répétait cette expérience de nombreuses fois avec des échantillons similaires, **95 % des intervalles calculés contiendraient la vraie moyenne de la population**.
