# %%
"""
1/ saisir n valeurs entiers relatifs dans le clavier séparés par ","
2/ on veut itérer sur les valeurs saisies pour vérifier
que ces valeurs sont des entiers relatifs (1er cas entier naturel ensuite 2ème cas négatif)
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 chiffres sign.  
"""

# %%

valeurs = input("saisir des entiers relatifs séparés par une virgule: ")
valeurs = valeurs.split(",")

# %% -------------------------- boucle for -----------------------------------
ints = []

for val in valeurs:
    val = val.strip() # enlever les espaces avant et après la valeur
    if val.is_numeric() or (val[0] == "-" and val[1:].is_numeric()):
        ints.append(int(val))
    else:
        print(f"{val} n'est pas un entier relatif. Arrêt de la saisie.")
        break

if ints:
    moyenne = round(sum(ints) / len(ints), 2)
    print(f"La moyenne des entiers saisis est: {moyenne:.2f}")
