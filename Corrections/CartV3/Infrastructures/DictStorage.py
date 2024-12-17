from typing import Dict

class DictStorage:

    def __init__(self):
        self.storage: Dict[str, float] = {}

    def set_value(self, name: str, value: float) -> None:

        if name in self.storage:
            self.storage[name] += value

            return

        self.storage[name] = value

    def get_value(self, name : str) -> float:
        
        if name not in self.storage :
            raise ValueError(f"je n'ai pas cette clé {name} dans mon storage ")
        
        
        return self.storage[name]
    
    def reset(self) -> None :
        
        self.storage.clear()
        
    def restore(self, name: str):
        if name not in self.storage :
            raise ValueError(f"je n'ai pas cette clé {name} dans mon storage ")
        
        del self.storage[name]
        