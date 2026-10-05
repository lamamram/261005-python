# %%
"""
1/ saisir n valeurs entiers relatifs dans le clavier séparés par ","
2/ on veut itérer sur les valeurs saisies pour vérifier
que ces valeurs sont des entiers relatifs (1er cas entier naturel ensuite 2ème cas négatif)
HINT: il y a une fonction interne des str qui vérifie si la str est numerique ?
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 chiffres sign.  
"""

# %%

valeurs = input("saisir des entiers relatifs séparés par une virgule: ")
valeurs = valeurs.split(",")

# %% -------------------------- boucle for -----------------------------------

