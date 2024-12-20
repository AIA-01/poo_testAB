### **QCM sur TCL, Loi Normale, Intervalle de Confiance, Test Z et ttest_ind**

#### 1. Le **théorème central limite (TCL)** stipule que :
- [X] Pour un grand nombre d'observations, la somme des variables suit une loi normale  
- [ ] La moyenne d'un échantillon suit toujours une loi normale  
- [ ] La variance d'un échantillon augmente avec la taille de l'échantillon  
- [ ] La distribution d'échantillon ne converge jamais vers une loi normale

#### 2. La loi normale est une distribution **symétrique** autour de sa **moyenne**, cela signifie que :
- [X] La moyenne, la médiane et le mode sont égaux  ( tout est centré autour de la valeur moyenne le haut de la courbe )
*Le calcul de la probabilité se fait à l'aide la courbe, elle correspond à l'air sous la courbe et l'axe des abscisses.* 
- [ ] Les données sont toujours centrées autour de zéro  
- [ ] L'écart-type doit être nul  
- [ ] Les données suivent nécessairement une distribution uniforme

#### 3. Un **intervalle de confiance** (IC) est utilisé pour :
- [ ] Fournir une estimation du taux de conversion  
- [ ] Mesurer la précision des résultats du test  
- [X] Estimer un paramètre de population avec une certaine marge d'erreur
* Si on prend Z = 1.96 sur l'axe des x une unité d'écart type, on définit une marge d'erreur 95% de chance de ne pas se tromper, 5% de chance de se tromper*
- [ ] Comparer la moyenne de deux groupes

#### 4. Le **test Z** est utilisé principalement lorsque :
- [X] L'échantillon est grand (n > 30) et la variance ( l'écart type c'est la racine carré de la variance) est connue ou approximée  
- [ ] L'échantillon est petit et la variance est inconnue  
- [ ] Les données ne suivent pas une loi normale  
- [ ] Vous comparez des échantillons appariés

#### 5. Dans quel cas utiliseriez-vous un **ttest_ind** ?
- [ ] Pour comparer les moyennes de deux échantillons indépendants de taille similaire  
- [ ] Pour comparer les proportions de deux échantillons  
- [ ] Pour comparer des échantillons appariés  
- [ ] Pour tester la normalité des données

#### 6. Le **test Z** est applicable lorsque :
- [ ] L'échantillon est petit et la variance est inconnue  
- [X] L'échantillon est grand et la variance est connue  
- [ ] Vous comparez des échantillons appariés  
- [ ] Vous comparez des proportions

#### 7. Le **théorème central limite (TCL)** devient de plus en plus applicable :
- [ ] Lorsque la taille de l'échantillon est inférieure à 30  
- [ ] Lorsque les données suivent une loi normale  
- [X] Lorsque la taille de l'échantillon est grande (n > 30)  
- [ ] Lorsque la variance des échantillons est infinie

#### 8. Un **intervalle de confiance à 95%** signifie que :
- [ ] Il y a 95% de chances que la valeur estimée soit exactement à l'intérieur de l'intervalle  
- [X] Si vous répétez l'expérience plusieurs fois, 95% des intervalles construits contiendront la véritable valeur du paramètre  
- [ ] L'intervalle est toujours symétrique  
- [ ] Vous pouvez conclure qu'il n'y a pas d'incertitude

#### 9. Le test **ttest_ind** compare :
- [ ] Les proportions de deux échantillons indépendants  
- [X] Les moyennes de deux échantillons indépendants  
- [ ] Les moyennes de deux échantillons appariés  
- [ ] La distribution des deux échantillons

#### 10. Si l'échantillon est petit et que vous devez comparer les moyennes de deux échantillons indépendants, vous utilisez :
- [ ] Test Z  
- [X] Test t de Student (ttest_ind)  
- [ ] Test de Kolmogorov-Smirnov  
- [ ] Test U de Mann-Whitney

#### 11. Le **test de Z** pour un échantillon est utilisé pour :
- [ ] Tester la normalité d'une distribution  
- [X] Comparer la moyenne d'un échantillon à une valeur de référence lorsque l'échantillon est grand et que la variance est connue  
- [ ] Comparer les moyennes de deux échantillons indépendants  
- [ ] Comparer les proportions entre deux groupes

#### 12. Le **théorème central limite (TCL)** implique que, à mesure que la taille de l'échantillon augmente :
- [ ] La distribution des échantillons devient de plus en plus plate  
- [ ] La variance de l'échantillon devient plus grande  
- [x] La distribution de la moyenne d'échantillon tend vers une loi normale  
- [ ] La distribution des échantillons devient de plus en plus asymétrique

#### 13. Si vous avez un échantillon de petite taille et que vous voulez comparer les moyennes de deux groupes indépendants, vous devez utiliser :
- [ ] Test Z  
- [ ] Test U de Mann-Whitney  
- [x] Test t de Student (ttest_ind)  
- [ ] Test de Wilcoxon

#### 14. Quel est le seuil de p-value généralement utilisé pour rejeter l'hypothèse nulle dans un test t (petit échantillon) / ou z ( échantillons n >= 30 )?
- [x] 0.05
*L'hypothèse nulle c'est : "pas de différence", si la proba est faible on la rejète donc on change le bouton, on a une erreur de 5% ( de chance de se tromper)*
- [ ] 0.10  
- [ ] 0.01  
- [ ] 0.50

#### 15. Le test **ttest_ind** suppose que les deux groupes :
- [ ] Ont la même variance  
- [x] Sont indépendants et ont des distributions normales  
- [ ] Ont des tailles d'échantillon égales  
- [ ] Sont appariés

#### 16. Quel est l'effet d'un **intervalle de confiance plus large** ?
- [ ] Il augmente la précision de la moyenne estimée  
- [x] Il indique que l'estimation de la moyenne est moins précise
*99% un intervalle plus grand dans lequelle la valeur rechercher se trouve, donc moins précis.*
- [ ] Il signifie que l'échantillon est plus grand  
- [ ] Il montre que la population suit une distribution normale

#### 17. Le **test Z** est souvent préféré pour les grands échantillons car :
- [ ] Il est plus adapté aux petits échantillons  
- [ ] Il ne nécessite pas de connaître la variance  
- [X] Il est plus fiable lorsque la taille de l'échantillon est grande et que la variance ou l'écart type est connue  
- [ ] Il est plus précis que le test t

#### 18. Le test **ttest_ind** (test t) peut être utilisé pour :
- [ ] Comparer des échantillons appariés  
- [ ] Comparer la variance de deux échantillons  
- [x] Comparer les moyennes de deux groupes indépendants  
- [ ] Tester l'adéquation à la loi normale

#### 19. Le test **t** de Student s'applique :
- [ ] Aux échantillons de grande taille uniquement  
- [ ] Aux échantillons avec des variances égales  
- [X] Aux échantillons de petite taille avec une variance inconnue  
- [ ] Lorsque les données sont non paramétriques

#### 20. Si la p-value d'un test Z est inférieure à 0.05, cela signifie :
- [ ] Les résultats sont dus au hasard  
- [ ] Les deux groupes sont exactement égaux  
- [x] Il y a suffisamment de preuves pour rejeter l'hypothèse nulle
*( avec un vaccin et une marge d'erreur de 5%, sur 100 personnes on aura 5 personnes probablement non couverte par le vaccin.  )*
- [ ] Le test est invalide

---
