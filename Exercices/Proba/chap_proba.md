### **Exercice 1 : Lancer un dé**
Simulez un lancer de dé à 6 faces. Faites une classe.

1. Écrivez un programme qui simule le lancer d'un dé à 6 faces et affiche le résultat.
2. Faites 1000 lancers et déterminez la fréquence d'apparition de chaque face.

---

### **Exercice 2 : Pile ou face**
Simulez une série de lancers de pièce.

1. Simulez 10 lancers d'une pièce et affichez le résultat pour chaque lancer (`Pile` ou `Face`).
2. Répétez cette simulation 1000 fois et calculez la proportion de `Pile` et de `Face`.
3. Comparez vos proportions avec la probabilité théorique (50 % pour chaque côté).

---

### **Exercice 3 : Combinaisons simples**
Tirez une carte d'un jeu de cartes standard.

1. Créez une liste représentant les 52 cartes d'un jeu.
2. Simulez le tirage aléatoire d'une carte.
3. Modifiez votre code pour simuler 10 tirages sans remise (chaque carte tirée est retirée du jeu).

---

### **Exercice 4 : Probabilité d'au moins une paire**
Simulez le tirage de 5 dés et calculez la probabilité d'obtenir au moins une paire.

1. Simulez un tirage de 5 dés et affichez le résultat.
2. Vérifiez s'il existe au moins deux dés avec le même nombre.
3. Répétez cette simulation 10 000 fois et estimez la probabilité d'obtenir au moins une paire.

---

### **Exercice 5 : Loi des grands nombres**
Montrez expérimentalement la loi des grands nombres.

1. Simulez le lancer d'une pièce 10 fois et calculez la proportion de `Pile`.
2. Répétez cette simulation pour 100, 1000, 10 000, puis 100 000 lancers.
3. Tracez un graphique de la proportion de `Pile` en fonction du nombre de lancers pour observer la convergence vers 0,5 (la probabilité théorique).

---

### Indications pour la résolution
Voici quelques fonctions utiles en Python pour ces exercices :

- **`random.randint(a, b)`** : génère un entier aléatoire entre `a` et `b`.
- **`random.choice(list)`** : choisit un élément aléatoire dans une liste.
- **`random.shuffle(list)`** : mélange une liste aléatoirement.
- **`collections.Counter`** : compte les occurrences d'éléments dans une liste.
- **`matplotlib.pyplot`** : pour tracer des graphiques dans l'exercice 5.
