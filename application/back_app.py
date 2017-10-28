#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Blueberry
  auteurs: michael
  version: 0.1
  date: 23/10/2017
'''

import logging
import configparser
import time

logging.basicConfig(filename='./log/blueberry.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from src.api.api_telegram import ApiTelegram
from src.scans.ping_scan import PingScan
from src.api.api_bdd import *

if __name__=="__main__":
    logging.info("Initialisation de Blueberry")
    try:
        while 1:
            scan_type = Parametre.get(Parametre.section == "scan",
                                      Parametre.key == "type").value
            scan_time = Parametre.get(Parametre.section == "scan",
                                      Parametre.key == "time_enter_scan").value
            logging.info("Demarrage d'un {} scan".format(scan_type))
            net = PingScan()
            net.start()
            time.sleep(int(scan_time))
    except KeyboardInterrupt:
        logging.info("Extinction de Blueberry")
        exit
