# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow/gpt)
hint: les zip s'ouvrent et se ferment

3. déplacer le fichier csv en dans data/dns.csv
4. ne faire ce qui précède qui si ce n'est pas déjà fait
hint: module os et pathlib.Path


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""

# %% ------------------ téléchargement du fichier zip ------------------

import requests

url = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
archive_name = url.split("/")[-1]

# GET, POST,  PUT,                    PATCH,    DELETE    , HEAD:                 : ce sont les VERBES ou METHODES HTTP
# lire, créer, modif complète, modif partielle, supprimer , réponse sans headers

try:

   r = requests.get(url)
   ## gérer l'objet Response
   # 1/ regarder le code de statut de la réponse: 2XX (OK), 3XX (redirect), 4XX (pb request), 5XX (pb server)
   if 200 <= r.status_code < 300:
      # regarder les entêtes de la réponse notamment le Content-Type (type de réponse)
      if r.headers["content-type"] == "application/zip":
         # regarder le contenu 
         # r.content (octets), 
         # r.text (text + encodage), 
         # r.raw (idem mais sans échappement), 
         # r.json() conversion depuis JSON
         with open(f"./{archive_name}", mode="wb") as f:
               f.write(r.content)
   else:
      raise ValueError(f"code statut en erreur: {r.status_code}")
# utiliser préférentiellement les exceptions incluses avec vos outils si elles existent
except (requests.ConnectionError, requests.HTTPError, ValueError) as e:
    print(e)




# %%
