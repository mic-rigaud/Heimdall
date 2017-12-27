from application.src.api.api_bdd import *
import configparser
import subprocess
import os

config = configparser.ConfigParser()
FNULL = open(os.devnull, 'w')

try:
    config.read('./config/config.ini')
    if not config:
        print('No config file found!')
        exit
except:
    print("=== Erreur lors de la lecture du fichier de configuration ===")

################################################################################
# Il faut verif les param dans config.ini
################################################################################

try:
    db.connect
    db.create_tables([Ip, Parametre])
    for sec in config:
        for element in config[sec]:
            print("= Ajout dans la table parametre de l element: " + sec + ", " + element + ",  " + config[sec][element])
            param = Parametre.create(section=sec, key=element, value=config[sec][element]).save()
except:
    print("=== La base SQL existe déjà ===")

try:
    subprocess.check_call(["mkdir","logs"], stderr=FNULL)
    print("= Creation du dossier logs")
except:
    print("=== Le dossier logs existe déjà ===")
