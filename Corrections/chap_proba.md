### **Correction de l'Exercice 1 : Lancer un dé**

```python
import random
from collections import Counter

class DiceSimulator:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)
    
    def roll_multiple(self, times):
        results = [self.roll() for _ in range(times)]
        
        return Counter(results)

# Utilisation
dice = DiceSimulator()
print("Résultat d'un lancer :", dice.roll())
print("Fréquences après 1000 lancers :", dice.roll_multiple(1000))
```

---

### **Correction de l'Exercice 2 : Pile ou Face**

```python
class CoinFlipSimulator:
    def __init__(self):
        self.sides = ['Pile', 'Face']
    
    def flip(self):
        return random.choice(self.sides)
    
    def flip_multiple(self, times):
        results = [self.flip() for _ in range(times)]
        return Counter(results)

# Utilisation
coin = CoinFlipSimulator()
print("10 lancers :", [coin.flip() for _ in range(10)])
print("Proportions après 1000 lancers :", coin.flip_multiple(1000))
```

---

### **Correction de l'Exercice 3 : Combinaisons simples**

```python
class CardDeck:
    def __init__(self):
        self.deck = [
            f"{rank} of {suit}" for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']for rank in range(1, 14)
        ]
    
    def draw_card(self):
        if not self.deck:
            return "Le deck est vide."
        card = random.choice(self.deck)
        self.deck.remove(card)

        return card
    
    def draw_multiple(self, n):
        return [self.draw_card() for _ in range(min(n, len(self.deck)))]

# Utilisation
deck = CardDeck()
print("Carte tirée :", deck.draw_card())
print("10 cartes tirées sans remise :", deck.draw_multiple(10))
```

---

### **Correction de l'Exercice 4 : Probabilité d'au moins une paire**

```python
class DicePairSimulator:
    def __init__(self, dice_count=5):
        self.dice_count = dice_count
    
    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(self.dice_count)]
    
    def has_pair(self, rolls):
        counts = Counter(rolls)
        return any(count >= 2 for count in counts.values())
    
    def simulate(self, trials):
        pair_count = sum(1 for _ in range(trials) if self.has_pair(self.roll_dice()))
        return pair_count / trials

# Utilisation
dice_pair_simulator = DicePairSimulator()
print("Probabilité d'au moins une paire après 10 000 essais :", dice_pair_simulator.simulate(10000))
```

---

### **Correction de l'Exercice 5 : Loi des grands nombres**

```python
import matplotlib.pyplot as plt

class LawOfLargeNumbers:
    def __init__(self):
        self.sides = ['Pile', 'Face']
    
    def flip(self):
        return random.choice(self.sides)
    
    def simulate(self, trials):
        pile_count = 0
        proportions = []
        for i in range(1, trials + 1):
            if self.flip() == 'Pile':
                pile_count += 1
            proportions.append(pile_count / i)
        return proportions
    
    def plot_simulation(self, trials):
        proportions = self.simulate(trials)
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, trials + 1), proportions, label="Proportion de Pile")
        plt.axhline(y=0.5, color='red', linestyle='dashed', label="Probabilité théorique (50%)")
        plt.xlabel("Nombre de lancers")
        plt.ylabel("Proportion de Pile")
        plt.title("Loi des grands nombres")
        plt.legend()
        plt.show()

# Utilisation
law_of_large_numbers = LawOfLargeNumbers()
law_of_large_numbers.plot_simulation(100000)
```

---
