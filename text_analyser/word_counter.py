# les imports inter packages DEVRAIENT être écrits à partir du package
# from text_analyser.text_cleaner import Cleaner
# ou à la rigueur en relatif
from .text_cleaner import Cleaner

class Counter:
    def __init__(self, cleaner: Cleaner, word_length: int=3):
        self.text = cleaner.clean(word_length)

    def count(self, nb_crop: int=5) -> dict:
        occurences = {}
        # pour chaque mot du texte (nettoyé)
        for word in self.text.split():
        # soit le mot est déjà dans le dictionnaire au quel cas j'incrémente son occurence
          if word in occurences:
              occurences[word] += 1 
        # soit le mot n'est pas dans le dictionnaire alors je créé la clé avec l'occurence 1
          else:
              occurences[word] = 1

        # trier par occurences
        # 1. transformer le dict en liste de tuples => .items
        # 2. trier avec une lambda pour trier sur les occurences décroissantes
        # 3. croper la liste de tuples [:nb_crop]
        # 4. on remet en dict
        return dict(sorted(
            occurences.items(), 
            key=lambda t: t[1],
            reverse=True
        )[:nb_crop])

