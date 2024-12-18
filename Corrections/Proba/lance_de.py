from random import randint
from collections import Counter

class DiceSimulator:
    def __init__(self, sides: int=6):
        self.sides = sides
        
    def roll(self)->int:
        return  randint(1, self.sides)
    
    def  roll_multiple(self, number : int ):
        results = []
        for i in range(number):
            results.append(self.roll())
            
        return Counter(results)
    
diceSimulator = DiceSimulator()

# simulation 
NB_LANCER = 1_000_000

for k, v in diceSimulator.roll_multiple(NB_LANCER).items():
    print(k, abs( v/NB_LANCER - 1/6) )


