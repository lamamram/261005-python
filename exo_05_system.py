# %% ------ utilisation du module standard subprocess ----------
"""
subprocess permet de créer un processus enfant à partir du processus
parent, i.e, le processus python en exécution.

on l'utilise dans le cas d'une commande qu'on ne peut pas faire avec 
les outils de bases de python => commandes très complexes !!!
=> vous avez os, sys, et autres avec pip
"""

import subprocess
import shlex

# je veux savoir les noms des fichiers .py dans le dossier courant

# 1. je vais lancer une commande bash ls -1 *.py ou ls -1 | grep .py
# 2. et je veux voir la réponse

cmd = "ls -1 *.py"
tokens = ["ls", "-1", "*.py"]
lex_tokens = shlex.split(cmd)
# WARN 1. attention pas de shell pas d'excutable on exécute dans un tty
# WARN 2. il est recommandé d'écrire la commande en tant que TOKENS 
# ==> interdit certaines injections de commandes
# WARN 3. en cas de commnandes complexes avec options complexes MAIS SANS PIPE
# ==> utiliser shlex (analyseur lexical)

result = subprocess.run(
  lex_tokens,
  # sortie en texte: ajouter un flux de sortie stdout
  capture_output=True,
  text=True)

# return code: 0 == OK , non-zero == ERREUR
print(result.returncode)
print(result.stdout.splitlines())


# %% -------------- idem avec os -------------------

import os


print(list(filter(lambda p: p.endswith(".py"), os.listdir("."))))

# for p in os.listdir("."):
#   if p.endswith(".py"):
#     print(p)


# %% -------------------- subprocess avec PIPE (SAFE) -----------------

# ls -1 | grep -E ".py$" => dans un bash
# shlex ne peut analyser une commande pipe car il pense que c'est une option

cmd1 = subprocess.Popen(shlex.split("ls -1"), stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(shlex.split(r'grep -E "\.py$"'), stdin=cmd1.stdout, stdout=subprocess.PIPE)
cmd1.stdout.close() # permet d'avoir le signal de sortie de cmd2 pour s'arrêter
output, _ = cmd2.communicate()
# output => octets => decode("utf-8") => str 
print(output.decode("utf-8").splitlines())


# %% --------------------------- surcouche subprocess pour les pies (powershell) --------------
# pip install sarge
"""
sarge simplifie les commandes | avec bash ou powershell
WARNING: les commandes | en powershell 
notamment avec des données d'entrées venant de l'utilisateurs (variables)
ne peuvent pas être complètement sécurisées => il faut valider avant d'exécuter
"""

import sarge
from typing import List

def run_ps(cmd: str, unique=False) -> str | List[str]:
  """
  pour des commandes pipes powershell sans donées d'entrée => commandes en dur
  """
  # 1. par défaut subprocess avec windows lance un cmd (invite DOS)
  invoke_cmd = ["powershell", "-NoProfile", "-OutputFormat", "Text", "-Command"]
  # 2. pb d'encodages avec powershell(windows) => utf8
  set_encoding_cmd = "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8"
  # 3. changement d'encodage + commande attendue
  cmd = ";".join([set_encoding_cmd, cmd])
  invoke_cmd.append(INTERFACES_CMD)
  output = sarge.capture_stdout(invoke_cmd).stdout.text
  
  return output if unique else output.splitlines()

INTERFACES_CMD = "Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty InterfaceDescription"

run_ps(INTERFACES_CMD)
# %%
