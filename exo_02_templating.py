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
    "pression": 500,
    "section": 30,
    "debit": 2
}

# %%
start_index = _template.index("((") + 2
end_index = _template.index("))")
key = _template[start_index:end_index]
print(key)

print(_template.replace("((" + key + "))", str(injections[key])))

# %%
# exemple avec for
for k, v in injections.items():
    _template = _template.replace("((" + k + "))", str(injections[k]))

print(_template)

# %%
# exemple avec while
while "((" in _template:
    start_index = _template.index("((") + 2
    end_index = _template.index("))")
    key = _template[start_index:end_index]

    _template = _template.replace("((" + key + "))", str(injections.get(key, "N/A")))

_template
# %% ----- portage de la cellule précédente en fonction ----------
"""
technique
1/ entourer le code avec l'entête de def et ajouter le nom
2/ transformer le print ou affectation finale en return
3/ réféchir sur les paramètres d'entrée (positionnels / centraux, et optionnels => valeur par défaut) et de sortie
4/ refactorer le code pour utiliser les paramètres d'entrée et construire la sortie
5/ tester dans différents cas
"""

def parse_template(
        tpl: str, data: dict, 
        # delimiters: tuple=("{{", "}}")
        delim_in:str="{{", 
        delim_out: str="}}", 
        default: str="N/A",
        **opts
    ) -> str:
    """
    fonction d'injection de données dans un template
    opts:
    - debug => True: mode debug
    """
    while delim_in in tpl:
        start_index = tpl.index(delim_in) + len(delim_in)
        end_index = tpl.index(delim_out)
        key = tpl[start_index:end_index]

        # mode debug
        if "debug" in opts and opts["debug"]:
            print(f"DEBUG: clé: {key}")
        
        tpl = tpl.replace(delim_in + key + delim_out, str(data.get(key, default)))

    return tpl

parse_template(_template, injections, delim_in="((", delim_out="))")

parse_template("blabla ... {{key}}", {"key": "value"}, debug=True)

# %%
