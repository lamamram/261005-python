# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.ZipFile (doc ou google/stackoverflow/gpt)
hint: les zip s'ouvrent et se ferment
hint: trouver les infos sur les éléments dans l'archive .namelist()

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
import os

url = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
archive_name = url.split("/")[-1]
dns_name = "dns.csv"

# GET, POST,  PUT,                    PATCH,    DELETE    , HEAD:                 : ce sont les VERBES ou METHODES HTTP
# lire, créer, modif complète, modif partielle, supprimer , réponse sans headers


# si l'archive n'est pas (plus) à la racine Alors on télécharge
if not os.path.exists(f"./{archive_name}"):
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




# %% -------------- décompression du zip + manip de système de fichier ----------------

from zipfile import ZipFile
from pathlib import Path

# utilisations des objets chemins portable
# dossier parent, fichier, extension
# p_data.absolute().parent, p_data.stem, p_data.suffix
# ROOT_DIR = Path(__file__).absolute().parent

p_data = Path("./data")
p_csv = p_data / dns_name


if not p_data.exists():
   # les objet Path sont complètement compatibles avec os
   os.mkdir(p_data)

if not p_csv.exists():
   with ZipFile(f"./{archive_name}", mode="r") as z:
      csv_name = z.namelist()[0]
      z.extract(csv_name, path=p_data)

   # l'opérateur '/' a été redéfini pour une concaténation entre objet Path ou entre Path <-> str
   os.rename(p_data / csv_name, p_csv)

# %% ------------ découper un gros csv -----------------------
"""
dans la boucle for:
- accumuler 100k lignes
- quand on sait qu'on est sur la 100kème ligne et aussi la 200kème ligne (multiple de 100k)
  + on créé un fichier de type f"dns_{num_ligne}.csv" dans lequel on écrit
  + le header et 100k lignes
- après le 2 paquets on s'arrête

"""

import csv

encoding = "utf-8"
delimiter = ";"
slice_size = 10**5
nb_slice = 2

def write_slice(num_line, header, rows: list):
   with open(p_data / f"dns_{num_line}.csv", mode="w", encoding=encoding) as f:
      writer = csv.writer(f, delimiter=delimiter, lineterminator="\n")
      writer.writerow(header)
      writer.writerows(rows)
      rows.clear() # vide rows qui est aussi le rows global
      # rows = [] # mauvais car ce rows change d'id !!! donc ne vide pas le rows global


rows = []

with open(p_csv, mode="r", encoding=encoding) as f:
   reader = csv.reader(f, delimiter=delimiter)
   header = next(reader)
   for num_line, row in enumerate(reader, start=1):
      if num_line > nb_slice * slice_size: break
      rows.append(row)
      if not num_line % slice_size:
         write_slice(num_line, header, rows)


# %% ------------------------ idem avec pandas ------------------------

# pip install pandas
import pandas as pd

dns_df = pd.read_csv(
   url, sep=delimiter, encoding=encoding
)
dns_df

# %%

dns_df.to_csv(
   "dns.zip",
   sep=';',
   encoding=encoding,
   index=False
)

# %%
"""
je veux voir les pays qui hébergent du .fr dans l'ordre croissant du compte
"""

dns_subset_df = pd.read_csv(
   "dns.zip",
   sep=delimiter,
   encoding=encoding,
   usecols=["Nom de domaine", "Pays BE"],
   # nrows=10**6
)

gb = dns_subset_df.groupby(by="Pays BE")
count_countruies_series = gb["Nom de domaine"].count().sort_values(ascending=False)
count_countruies_series
# %%
