# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

3. déplacer le fichier csv en dans data/dns.csv
4.. ne faire ce qui précède qui si ce n'est pas déjà fait
hint: module os et pathlib.Path


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""

import sys

import requests
import os
from pathlib import Path
from zipfile import ZipFile

URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
DNS_NAME = "dns.csv"

archive_name = URL.split("/")[-1]
p_archive = Path(f"./{archive_name}")

# if not os.path.exists(f"./{archive_name}")
if not p_archive.exists():
   try:
      # requête http de type GET de l'url qui retourne une réponse http
      response = requests.get(URL)

      # regarde de code de retour de la réponse
      if 200 <= response.status_code < 300:
      # regarde le type de donées
         if "application/zip" in response.headers["content-type"]:
         # response.content contient l'archive en octets
         # wb = création avec contenu binaire
            with open(f"./{archive_name}", mode="wb") as f:
               f.write(response.content)
      # en cas de mauvais code
      else:
         raise ValueError(f"réponse en erreur : {response.status_code}")
   except (requests.ConnectionError, ValueError) as e:
      print(e)
      sys.exit()

p_data = Path("./data")
if not p_data.exists():
  os.mkdir(p_data)

if not (p_data / DNS_NAME).exists():
   with ZipFile(p_archive) as zf:
      names = zf.namelist()
      zf.extract(names[0], path=p_data)
      os.rename(p_data / names[0], p_data / DNS_NAME)

# %%
import csv

NB_ROWS = 10**5
NB_SLICES = 2

rows = []

with open(p_data / DNS_NAME, "r", encoding="utf-8") as f:
   reader = csv.reader(f, delimiter=";")
   header = next(reader)
   for i, row in enumerate(reader, start=1):
      if i > NB_SLICES * NB_ROWS: break
      rows.append(row)
      if i % NB_ROWS: continue
      # pas de conflit entre f et wf
      with open(p_data / f"dns_{i}.csv", "w", encoding="utf-8") as wf:
         writer = csv.writer(wf, delimiter=";", lineterminator="\n")
         writer.writerow(header)
         writer.writerows(rows)
         rows = []


# %% ---------------------------- idem avec pandas -----------------------------

import pandas as pd

URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
DNS_NAME = "dns.csv"

# créer un DataFrame à partr d'un fichier csv archivé sur une machine distante
dns_df = pd.read_csv(URL, sep=";", encoding='utf-8')
dns_df




# %%
dns_df.to_csv(
   "dns.zip", 
   sep=";", 
   encoding="utf-8", 
   index=False,
   compression={
      "archive_name": "dns.csv",
      "method": "zip"
   }
)
# %%
dns_subset_df = pd.read_csv(
  "dns.zip",
  sep=";",
  encoding="utf-8",
  nrows=1000000,
  usecols=["Nom de domaine", "Pays BE"]
)
# %%
# regarde les pays les plus nombreux dans ce fichier
gb =dns_subset_df.groupby("Pays BE")
count_df = gb["Nom de domaine"].count().sort_values(ascending=False)
count_df
# %% ---------------------- tranche de 100k one shot -------------------------

import pandas as pd
URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
pd.read_csv(
   URL, 
   sep=";", 
   encoding='utf-8', 
   usecols=["Nom de domaine", "Pays BE"],
   nrows=10**5).to_csv("dns_100k.csv", sep=";", index=False, encoding="utf-8")

# %%
