from typing import Dict

class Counter:
    
    def __init__(self, message : str):
        self.message = message
        
    def letters(self) -> set :
        
        return set( self.message )
    
    def structure(self) -> Dict[str, int]:
        
        return { letter : self.message.count(letter) for letter in self.letters() } 
    

c = Counter("Mississippi")

print(c.letters())
print(c.structure())