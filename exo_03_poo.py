"""
1. créer un package (dossier) "text_analyser"
2. ajouter 2 modules "text_cleaner.py" et "word_counter.py"
3. dans text_cleaner.py créer une classe "Cleaner"
   - instancié avec un paramètre "text"
   - le texte est nettoyé des signes de ponctuation => string.punctuation
   - //                   des sauts de lignes (linux / windows)
   - //                   des mots de longueur inférieure ou égale à 3
   - une méthode publique "clean" retourne le texte nettoyé en minuscule

4. dans word_counter.py créer une classe "Counter"
   - instancié avec un paramètre "text"
   - utilise le cleaner pour nettoyer le texte
   - transforme le texte nettoyé en un dictionnaire contenant: 
     + les mots uniques du texte comme clés
     + le nb d'occurence des mots en clé dans le texte
   - une méthode publique "count" affiche les n mots les plus fréquents du texte par ordre décroissant

5. écrire le programme principal pour utiliser le package
"""

# from text_analyser.text_cleaner import Cleaner
# from text_analyser.word_counter import Counter

# avec import depuis le package (__init__.py)
from text_analyser import Cleaner, Counter

# sys.argv : permet de demander des paramètre dans le script depuis la cli
import sys

word_length = int(sys.argv[1]) if len(sys.argv) > 1 else 3
nb_crop = int(sys.argv[2]) if len(sys.argv) > 2 else 5


if __name__ == "__main__":
  text = """
Python est un langage de programmation interprété, 
multiparadigme et multiplateformes. 
Il favorise la programmation impérative structurée, 
fonctionnelle et orientée objet. 
Il est doté d'un typage dynamique fort, 
d'une gestion automatique de la mémoire par ramasse-miettes 
et d'un système de gestion d'exceptions ; 
il est ainsi similaire à Perl, Ruby, Scheme, 
Smalltalk et Tcl.
Le langage Python est placé sous 
une licence libre proche de la licence BSD et fonctionne sur la plupart des plateformes informatiques, 
des smartphones aux ordinateurs centraux, 
de Windows à Unix avec notamment GNU/Linux en passant 
par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. 
Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et 
une syntaxe simple à utiliser. 
"""
  cl = Cleaner(text)
  # print(cl.clean())
  counter = Counter(cl, word_length)
  print(counter.count(nb_crop))

  
