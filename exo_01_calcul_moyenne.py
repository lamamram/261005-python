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

valeurs_converties = []
for valeur in valeurs:
    valeur = valeur.strip() # le trim en python
#     if valeur.isnumeric() or ( valeur[0] == "-" ):
    # positif             OU  négatif: commence par - ET le reste est numérique
    if valeur.isnumeric() or ( valeur.startswith("-") and valeur[1:].isnumeric() ):
        valeurs_converties.append(int(valeur))
    else:
        print(f"Valeur non convertible: {valeur}")
        break


# si la liste n'est pas vide, autrement dit != []
if valeurs_converties:
    moyenne = round(sum(valeurs_converties) / len(valeurs_converties), 2)
    # print(f"Moyenne: {moyenne:.2f}")
    print(f"Moyenne: {moyenne}")

# %%
