from application.src.api.api_bdd import *
import configparser
import subprocess

config = configparser.ConfigParser()
config.read('./config/config.ini')
if not config:
    print('No config file found!')
    exit

################################################################################
# Il faut verif les param dans config.ini
################################################################################


db.connect
db.create_tables([Ip, Parametre])
for sec in config:
    for element in config[sec]:
        print(sec + " " + element + "  " + config[sec][element])
        param = Parametre.create(section=sec, key=element, value=config[sec][element]).save()
        print(param)


subprocess.call(["mkdir","logs"])
