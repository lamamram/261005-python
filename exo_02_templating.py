# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": "500",
    "section": "30",
    "debit": "2"
}

# %%

while "((" in _template:
  index_start = _template.find("((") + 2
  index_end = _template.find("))")
  key = _template[index_start:index_end]
  _template = _template.replace("((" + key + "))", injections.get(key, "N/A"))

print(_template)
# %% ----- portage de la cellule précédente en fonction ----------
"""
technique
1/ entourer le code avec l'entête de def et ajouter le nom
2/ transformer le print ou affectation finale en return
3/ réféchir sur les paramètres d'entrée (positionnels / centraux, et optionnels => valeur par défaut) et de sortie
4/ refactorer le code pour utiliser les paramètres d'entrée et construire la sortie
5/ tester dans différents cas
"""

DEBUG = True

def parse_template(
    tpl: str, 
    data: dict, 
    delims: tuple=("{{", "}}"), 
    default="N/A",
    **opts
) -> str:
  while delims[0] in tpl:
    index_start = tpl.find(delims[0]) + len(delims[0])
    index_end = tpl.find(delims[1])
    key = tpl[index_start:index_end]
    if "debug" in opts and opts["debug"]:
        print(f"key trouvée: {key}")
    tpl = tpl.replace(delims[0] + key + delims[1], str(data.get(key, default)))

  return tpl

print(parse_template(_template, injections, delims=("((", "))")))

print(parse_template("blabla {{value}}", {"value": 50}, debug=DEBUG))

# %%
