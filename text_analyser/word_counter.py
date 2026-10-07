# les imports inter packages DEVRAIENT être écrits à partir du package
# from text_analyser.text_cleaner import Cleaner
# ou à la rigueur en relatif
from .text_cleaner import Cleaner

class Counter:
    def __init__(self, cleaner: Cleaner, word_length: int=3):
        self.text = cleaner.clean(word_length)
