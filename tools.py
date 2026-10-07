DEBUG = True

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


if __name__ == "__main__":
    print("coucou")