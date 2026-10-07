from string import punctuation
import re

class Cleaner:
    def __init__(self, text: str):
        self.text = text

    def __remove_punctuation(self):
        self.text = re.sub(f"[{punctuation}]"," ", self.text)

    def __remove_crlf(self):
        # en python on peut utiliser une chaine de caractère "brut" raw
        self.text = re.sub(r"[\r\n]", " ", self.text)

    def __remove_big_spaces(self):
        self.text = re.sub(r"\s+", " ", self.text)

    def clean(self):
        self.__remove_punctuation()
        self.__remove_crlf()
        self.__remove_big_spaces()
        return self.text.lower()