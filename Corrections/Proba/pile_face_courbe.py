import random
from collections import Counter
import matplotlib.pyplot as plot

class CoinSimulator:
    def __init__(self):
        self.sides = ["pile", "face"]

    def flip(self):
        return random.choice(self.sides)

    def flip_multiple(self, num: int = 100, repetition : int = 1_0000):
        
         return  [ sum( self.flip() == "pile" for _ in range(num) ) for _ in range(repetition) ]

c = CoinSimulator()

plot.figure( figsize=(10, 6) )
plot.hist(c.flip_multiple(), bins=20  )