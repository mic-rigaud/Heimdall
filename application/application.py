# @Author: michael
# @Date:   01-Dec-2017
# @Project: Blueberry
# @Filename: application.py
# @Last modified by:   michael
# @Last modified time: 08-Apr-2018
# @License: GNU GPL v3

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import time

from application.src.api.api_bdd import *
from application.src.api.api_telegram import ApiTelegram
from application.src.scans.arp_scan import ArpScan
from application.src.scans.ping_scan import PingScan


def application_main():
    logging.info("Initialisation de Blueberry")
    try:
        while 1:
            scan_type = Parametre.get(Parametre.section == "scan",
                                      Parametre.key == "scan_type").value
            scan_time = Parametre.get(Parametre.section == "scan",
                                      Parametre.key == "time_enter_scan").value
            logging.info("Demarrage d'un {} scan".format(scan_type))
            if scan_type == "ping":
                net = PingScan()
            elif scan_type == "arp":
                net = ArpScan()
            else:
                logging.critical(
                    "Erreur dans la configuration. Le type de scan " +
                    scan_type + " n'existe pas.")
                exit()
            net.start()
            time.sleep(int(scan_time))
    except KeyboardInterrupt:
        logging.info("Extinction de Blueberry")
        logging.shutdown()
        exit()
