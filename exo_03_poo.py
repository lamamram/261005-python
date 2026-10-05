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

# import text_analyser.text_cleaner as tc
from text_analyser.text_cleaner import Cleaner
from text_analyser.word_counter import Counter

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

# tc.Cleaner()

########### techniques d'associations possibles entre classes ###############
## 1. deux classes indédenpantes
# avantages: maintenabilité et réutilisabilité max 0 couplage entre les 2
# inconvénient: du point de vue métier le counter ne foncitonne pas avec un texte non nettoyer
# => c'est le programme principal qui a la résponsabilité d'associer

# cleaner = Cleaner(text)
# clean_text = cleaner.clean()

# counter = Counter(clean_text)

## 2. composition : couplage fort

# counter = Counter(text)
# print(counter.get_occurences())

## 3. aggrégation: couplage faible et injection de dépendances

counter = Counter(Cleaner(text))
print(counter.get_occurences())
