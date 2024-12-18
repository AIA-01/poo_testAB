from random import choice
from collections import Counter

class CardDesk:

    def __init__(self):
        self.desks = [ f"{n} {color}" for color in ["Ca", "Co" , "P", "T"] for n in range(1, 14) ]

    def flip(self):
        return choice(self.desks)

    def flip_remove(self):

        if not self.desks:
            return None

        desk = self.flip()
        self.desks.remove(desk)

        return desk

    def flip_multiple(self, n : int, discount = False):

        if discount == False:
            return Counter( [ self.flip() for _ in range(n) ] ) 

        return Counter( [ self.flip_remove() for _ in range(n) ] ) 
