import random
from collections import Counter

class CoinSimulator:
    def __init__(self):
        self.sides = ["pile", "face"]

    def flip(self):
        return random.choice(self.sides)

    def flip_multiple(self, number):
        result = []
        for _ in range(number):
            result.append(self.flip())

        return Counter(result)


c = CoinSimulator()

print(c.flip_multiple(100))
