# module de regex
import re 

words = """
Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace
lui doive être plus haïssable encore.

Henri Michaux
"""

class AnalyseContent:
    
    def __init__(self, words : str):
        self.words = words 
        
    def occurenceWord(self, letter: str)->int:
        
        # findall recherche sur toute la chaine de caractères
        # r pour considérer la chaine brut 
        # f interpollation -> insérer une variable dans la chaine de caractères
        # \b ce qui est adjacent et qui n'est pas alaphanumérique 
        # findall retourne une liste
        #print(re.findall(rf'\b{letter}\b', self.words))
        
        return len( re.findall(rf'\b{letter}\b', self.words) )
    
    def deleteLetter(self, word: str)->None:
        
        self.words = self.words.replace(word, "")
    

# En python on peut nommer les paramètres 
analyseC = AnalyseContent(words=words)

print( analyseC.occurenceWord("le") )

analyseC.deleteLetter("e")

print(analyseC.words)