#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 Strawberry
  auteurs: michael
  version: 0.1
  date: 13/05/2017
'''

import logging
import time
import yaml
from Strawberry.lib import network
from Strawberry.lib import myyaml

logging.basicConfig(filename='/home/michael/Documents/Programation/Strawberry/log/heimdall.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

NETWORKSTATUS = myyaml.myyaml()
FICHIER_OUTPUT = "output.yaml"
FICHIER_CONFIG = "config/strawberry.yaml"
NETWORKSTATUS.read(FICHIER_OUTPUT)
try:
    with open(FICHIER_CONFIG) as outline:
        CONFIG = yaml.load(outline)
except Exception as e:
    logging.error("Erreur lors de la lecture du fichier yaml. Message d'erreur: " + str(e))


def main():
    logging.info("Démarage du service")
    a=0
    while a<1:
        network_status = network.scan()
        NETWORKSTATUS.load(network_status)
        NETWORKSTATUS.write(FICHIER_OUTPUT)
        a=a+1
        time.sleep(CONFIG["time"])
    logging.info("Fin du service")


if __name__=="__main__":
    main()
