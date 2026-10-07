# les imports inter packages DEVRAIENT être écrits à partir du package
# from text_analyser.text_cleaner import Cleaner
# ou à la rigueur en relatif
from .text_cleaner import Cleaner

class Counter:
    def __init__(self, cleaner: Cleaner, word_length: int=3):
        self.text = cleaner.clean(word_length)

    def count(self) -> dict:
        occurences = {}
        # pour chaque mot du texte (nettoyé)
        for word in self.text.split():
        # soit le mot est déjà dans le dictionnaire au quel cas j'incrémente son occurence
          if word in occurences:
              occurences[word] += 1 
        # soit le mot n'est pas dans le dictionnaire alors je créé la clé avec l'occurence 1
          else:
              occurences[word] = 1
        return occurences 

