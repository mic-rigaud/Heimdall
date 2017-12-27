#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Blueberry
  auteurs: michael
  version: 0.1
  date: 23/10/2017
'''

import logging
import time

from application.src.api.api_telegram import ApiTelegram
from application.src.api.api_bdd import *

from application.src.scans.ping_scan import PingScan
from application.src.scans.arp_scan import ArpScan

def main():
    logging.info("Initialisation de Blueberry")
    try:
        while 1:
            scan_type = Parametre.get(Parametre.section == "scan",
                                      Parametre.key == "type").value
            scan_time = Parametre.get(Parametre.section == "scan",
                                      Parametre.key == "time_enter_scan").value
            logging.info("Demarrage d'un {} scan".format(scan_type))
            if scan_type == "ping":
                net = PingScan()
            elif scan_type == "arp":
                net = ArpScan()
            else:
                logging.critical("Erreur dans la configuration. Le type de scan " +
                                scan_type + " n'existe pas.")
                exit()
            net.start()
            time.sleep(int(scan_time))
    except KeyboardInterrupt:
        logging.info("Extinction de Blueberry")
        logging.shutdown()
        exit()
